const photos = [
    {
        keywords: ["allow", "accept", "allowed"],
        url: "./media/allow.jpg"
    },
    {
        keywords: ["baby", "babies", "child"],
        url: "./media/baby.jpg"
    },
    {
        keywords: ["breathing", "breath", "breaths"],
        url: "./media/breath.jpg"
    },
    {
        keywords: ["come", "call", "comes"],
        url: "./media/come.jpg"
    },
    {
        keywords: ["delete", "remove", "destroy"],
        url: "./media/delete.jpg"
    },
    {
        keywords: ["good luck", "okay", "good"],
        url: "./media/good luck.jpg"
    },
    {
        keywords: ["help", "help me", "helps"],
        url: "./media/help.jpg"
    },
    {
        keywords: ["snow", "winter", "cold"],
        url: "./media/photo8.jpg"
    },
    {
        keywords: ["garden", "flowers", "spring"],
        url: "./media/photo9.jpg"
    },
    {
        keywords: ["autumn", "leaves", "fall"],
        url: "./media/photo10.jpg"
    }
];

document.getElementById('search-button').addEventListener('click', function() {
    const searchTerm = document.getElementById('search-bar').value.trim().toLowerCase();
    const photoContainer = document.getElementById('photo-container');
    photoContainer.innerHTML = ''; // Clear any previous images

    const matchingPhoto = photos.find(photo =>
        photo.keywords.some(keyword => keyword.includes(searchTerm))
    );

    if (matchingPhoto) {
        const img = document.createElement('img');
        img.src = matchingPhoto.url;
        img.alt = searchTerm;
        img.style.display = 'block';
        photoContainer.appendChild(img);
    }
});

