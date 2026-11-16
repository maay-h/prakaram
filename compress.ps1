Add-Type -AssemblyName System.Drawing

$sourceDir = 'd:\Madhurya\Projects\Client Projects\prakaram\images\main'
$destDir = 'd:\Madhurya\Projects\Client Projects\prakaram\images\compressed'

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
}

$files = Get-ChildItem -Path $sourceDir -File | Where-Object { $_.Extension -match '\.(jpg|jpeg|png)$' }

foreach ($file in $files) {
    $destFile = Join-Path $destDir ($file.BaseName + '.jpg')
    if (Test-Path $destFile) {
        Write-Host "Skipping $($file.Name), already exists."
        continue
    }

    try {
        $img = [System.Drawing.Image]::FromFile($file.FullName)
        
        # Max width for high-res screens is ~1600px.
        $maxWidth = 1600
        $newWidth = $img.Width
        $newHeight = $img.Height

        if ($img.Width -gt $maxWidth) {
            $newWidth = $maxWidth
            $newHeight = [math]::Round(($maxWidth / $img.Width) * $img.Height)
        }

        $bmp = New-Object System.Drawing.Bitmap $newWidth, $newHeight
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        
        $g.DrawImage($img, 0, 0, $newWidth, $newHeight)

        # Set JPEG quality to 80
        $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageDecoders() | Where-Object { $_.FormatID -eq [System.Drawing.Imaging.ImageFormat]::Jpeg.Guid }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]80)
        
        $bmp.Save($destFile, $encoder, $encoderParams)
        
        $g.Dispose()
        $bmp.Dispose()
        $img.Dispose()
        
        Write-Host "Compressed $($file.Name)"
    } catch {
        Write-Host "Error compressing $($file.Name): $_"
    }
}
