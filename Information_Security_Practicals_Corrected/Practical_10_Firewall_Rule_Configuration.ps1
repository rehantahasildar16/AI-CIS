# PRACTICAL 10: Windows Firewall rule demonstration
# Run PowerShell as Administrator.

#Write-Host "===== Windows Firewall Profiles ====="
Get-NetFirewallProfile

#Write-Host "`n===== Creating Block Rule for TCP 8080 ====="
New-NetFirewallRule -DisplayName "Block TCP 8080" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Block

#Write-Host "`n===== Verifying Firewall Rule ====="
Get-NetFirewallRule -DisplayName "Block TCP 8080"

#Write-Host
 "`nRule is active. To remove it, run:"

#Write-Host 
'Remove-NetFirewallRule -DisplayName "Block TCP 8080"'