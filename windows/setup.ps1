function Invoke-GitClone($url) {
  $name = $url.Split('/')[-1].Replace('.git', '')
  & git clone $url $name | Out-Null
  Set-Location $name
}

# Check if Chocolately is installed
$ChocoInstalled = $false
if (Get-Command choco.exe -ErrorAction SilentlyContinue) {
    $ChocoInstalled = $true
}

if ($ChocoInstalled -eq $false) {
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Open text file of packages to install
Try {
$packages = Get-Content .\requirements.txt -ErrorAction Stop
}

Catch {
  write-host "Package requirements.txt is missing."
  break
}

# Install each package 
ForEach ($PackageName in $Packages) {
  if ($PackageName -match "^#" or $PackageName -match "")
    continue
  else 
    choco install $PackageName -y
}


Invoke-GitClone("https://github.com/Sycnex/Windows10Debloater")
.\Windows10SysPrepDebloater.ps1 -SysPrep -Debloat

# Invoke-GitClone("https://github.com/Disassembler0/Win10-Initial-Setup-Script")

# Enable wsl
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

sfc /scannow