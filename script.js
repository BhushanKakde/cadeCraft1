// Swipe gestures for navigation
const sections = document.querySelectorAll('section');

document.addEventListener('touchstart', handleTouchStart, false);
document.addEventListener('touchmove', handleTouchMove, false);

let xDown = null;
let yDown = null;

function handleTouchStart(evt) {
    xDown = evt.touches[0].clientX;
    yDown = evt.touches[0].clientY;
}

function handleTouchMove(evt) {
    if (!xDown || !yDown) {
        return;
    }

    let xUp = evt.touches[0].clientX;
    let yUp = evt.touches[0].clientY;

    let xDiff = xUp - xDown;
    let yDiff = yUp - yDown;

    if (Math.abs(xDiff) > Math.abs(yDiff)) {
        if (xDiff > 0) {
            // Swipe right
            navigatePrev();
        } else {
            // Swipe left
            navigateNext();
        }
    }

    xDown = null;
    yDown = null;
}


function navigatePrev() {
    const currentSection = document.querySelector('.active');
    const prevSection = currentSection.previousElementSibling;

    if (prevSection) {
        currentSection.classList.remove('active');
        prevSection.classList.add('active');
    }
}

function navigateNext() {
    const currentSection = document.querySelector('.active');
    const nextSection = currentSection.nextElementSibling;

    if (nextSection) {
        currentSection.classList.remove('active');
        nextSection.classList.add('active');
    }
}

// Initialize the first section as active
sections[0].classList.add('active');
