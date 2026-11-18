# Authoring only: no runtime dependency on System.Speech or voice installation.
param([string]$Unit = 'u11', [switch]$Force)
$ErrorActionPreference = 'Stop'
if ($Unit -notmatch '^u[0-9]{2}$') { throw 'Invalid unit key' }
$miaAudioFolder = Join-Path $PSScriptRoot "../generator/english/$Unit/audio"
$miaManifest = Get-Content -LiteralPath (Join-Path $miaAudioFolder 'manifest.json') -Raw -Encoding UTF8 | ConvertFrom-Json
Add-Type -AssemblyName System.Speech
$miaVoice = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
    $miaVoice.SelectVoice($miaManifest.voice)
    $miaVoice.Rate = $miaManifest.rate
    $miaFormat = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(22050, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono)
    foreach ($miaClip in $miaManifest.clips) {
        $miaTarget = Join-Path $miaAudioFolder $miaClip.file
        if ((Test-Path -LiteralPath $miaTarget) -and -not $Force) { continue }
        $miaVoice.SetOutputToWaveFile($miaTarget, $miaFormat)
        if ($miaClip.text -cmatch '^[A-Z]$') {
            $miaPrompt = New-Object System.Speech.Synthesis.PromptBuilder([System.Globalization.CultureInfo]::GetCultureInfo('en-US'))
            $miaPrompt.AppendTextWithHint($miaClip.text, [System.Speech.Synthesis.SayAs]::SpellOut)
            $miaVoice.Speak($miaPrompt)
        } else { $miaVoice.Speak($miaClip.text) }
        $miaVoice.SetOutputToNull()
    }
    Write-Output "Audio ready: $($miaManifest.clips.Count) clips ($Unit)"
} finally { $miaVoice.Dispose() }
