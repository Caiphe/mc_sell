$(document).ready(function () {
    // alert('Hello');

    $('.add-to-cart-a').click(function () {
        $("#cart-panet").removeClass('slideOutRight');
        $("#cart-panet").css('width', '300');
        $("#cart-panet").addClass('slideInRight')
    })

    $('.close-panel').click(function () {
        $("#cart-panet").removeClass('slideOutRight');
        $("#cart-panet").addClass('slideOutRight')
    })
})

// Loader hide
var loader = document.querySelector('.loader-container');
var addToCartbtn = document.querySelector('.cart-item-count');

addToCartbtn.addEventListener(click, function () {
    loader.classList.remove('.slideOutRight')
})

setTimeout(function () {
    loader.classList.add("slideOutRight")
}, 5000);

// $(document).ready(function () {
//     loader.classList.remove('.slideOutRight')
// })

setTimeout(function () {
    $('#my_custom_alert').removeClass('slideInLeft')
    $('#my_custom_alert').addClass('slideOutLeft')
}, 4000);