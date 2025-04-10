if (Get-Content "C:\Windows\System32\drivers\etc\hosts" | Select-String "127\.0\.0\.1") {
    Write-Output "Everything ok"
} else {
    Write-Output "ERROR! 127.0.0.1 is not in the hosts file"
}

# to run ou execute
# .\while_powershell.ps1