# PowerShell Script: List all running processes
Get-Process | Select-Object ProcessName, Id, CPU, StartTime | Format-Table -AutoSize
