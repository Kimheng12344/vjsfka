function downloadVideo() {
    const videoUrl = document.getElementById('videoUrl').value;
    // Here, you would implement the logic to process the video URL and generate a download link
    // For simplicity, let's assume the download link is directly provided here
    const downloadLink = `<a href="${videoUrl}" download>Download Video</a>`;
    document.getElementById('downloadLink').innerHTML = downloadLink;
}
