var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('default', ['start', 'watch']);

gulp.task('start', shell.task(['python league.py']));

gulp.task('watch', () => {
  return gulp.watch('league.py', ['reload'])
});

gulp.task('reload', () => {
  gulp.src('league.py')
    .pipe(shell(['python league.py']));
});