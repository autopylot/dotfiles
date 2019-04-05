function Invoke-GitClone($url) {
  $name = $url.Split('/')[-1].Replace('.git', '')
  & git clone $url $name | Out-Null
  Set-Location $name
}

Invoke-GitClone("https://github.com/Sycnex/Windows10Debloater")
.\Windows10SysPrepDebloater.ps1 -SysPrep -Debloat