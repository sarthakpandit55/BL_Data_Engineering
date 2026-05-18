from pydantic import BaseModel, field_validator, model_validator,SecretStr

class User(BaseModel):
    username: str
    password: SecretStr
    confirm_password: SecretStr

    @field_validator('username')
    @classmethod
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v

    @model_validator(mode='after')  
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


signup_data = User(**{"username":"rohan","password":"sarthak","confirm_password":"sarthak"})
print(signup_data)