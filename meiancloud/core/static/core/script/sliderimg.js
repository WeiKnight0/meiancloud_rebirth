document.addEventListener('DOMContentLoaded', function() {
    var imgs = document.querySelectorAll('.fade-in-image');

    imgs.forEach(img=>{
    var observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                img.classList.add('visible');
            } else {
                img.classList.remove('visible');
            }
        });
    }, {
        rootMargin: '0px',
        threshold: 0.6
    });

    observer.observe(img);
    });
});
