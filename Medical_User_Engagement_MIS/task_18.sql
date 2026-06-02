pg_dump -U postgres -d TASK_MIS_APP -F c -f "C:\mis_data\MIS_APP.backup" --for backup ADD

pg_restore -U postgres -d TASK_MIS_APP_RESTORE "C:\mis_data\MIS_APP.backup" --for restore the DATABASE