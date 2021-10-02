del /Q c:\Backup\test.bak
for /f "delims=." %%I in ("%date%") do del /Q c:\Backup\test_%%I.tar.gz
sqlcmd -i backup.sql
for /f "delims=." %%I in ("%date%") do tar -czf c:\Backup\test_%%I.tar.gz c:\Backup\test.bak
for /f "delims=." %%I in ("%date%") do curl -T c:\Backup\test_%%I.tar.gz ftp://backup:backup@192.168.1.123
