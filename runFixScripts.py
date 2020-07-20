import subprocess

output=subprocess.check_output('dir /b/a-d/od/t:c',shell=True)
output=output.decode("utf-8").split()

powershell_string = 'powershell & \\Users\\VssAdministrator\\AppData\\Local\\Microsoft\\AzSKLogs\\Sub_Azure subscription 1\\'+ output[-1]+ '\\FixControlScripts\\RunFixScripts.ps1'
print(powershell_string)
output = subprocess.check_output(powershell_string)

print(output)
