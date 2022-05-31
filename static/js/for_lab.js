const dfd1 = $.Deferred();
const dfd2 = $.Deferred();

$(".red").fadeOut(2000, dfd1.resolve);
$(".blue").fadeOut(5000, dfd2.resolve);

dfd1.done(function () {
 console.log("Красный квадрат скрыт");
});
dfd1.fail(function () {
 console.log("Красный квадрат НЕ скрыт");
});
dfd2.done(function () {
 console.log("Синий квадрат скрыт");
});
dfd2.fail(function () {
 console.log("Синий квадрат НЕ скрыт");
});
$.when(dfd1, dfd2).done(function () {
 console.log('Оба квадрата скрыты');
});