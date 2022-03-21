import { MDCSnackbar } from '@material/snackbar';
import { MDCSwitch } from '@material/switch';
const snackbar = new MDCSnackbar(document.querySelector('.mdc-snackbar'));
console.log(snackbar);
setTimeout(
    function() {
		snackbar.open();
}, 1000);
setTimeout(
    function() {
     snackbar.close()
}, 5000);


for (const el of document.querySelectorAll('.mdc-switch')) {
  const switchControl = new MDCSwitch(el);
}