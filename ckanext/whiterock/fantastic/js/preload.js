function preload(arrayOfImages) {
    $(arrayOfImages).each(function(){
        $('<img/>')[0].src = this;
    });
}


preload([
    '/images/cat-hover/Financial.png',
    '/images/cat-hover/Business-and-Economy.png',
    '/images/cat-hover/Census-Data.png',
    '/images/cat-hover/Community.png',
    '/images/cat-hover/Environment.png',
    '/images/cat-hover/Imagery.png',
    '/images/cat-hover/Infrastructure.png',
    '/images/cat-hover/Local-Government.png',
    '/images/cat-hover/Maps.png',
    '/images/cat-hover/Ocean.png',
    '/images/cat-hover/Planning.png',
    '/images/cat-hover/Transportation.png'
]);
