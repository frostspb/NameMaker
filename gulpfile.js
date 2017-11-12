var gulp = require('gulp');

var gulp = require('gulp');
var concat = require('gulp-concat');
var minifyCSS = require('gulp-minify-css');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var order = require('gulp-order');

var jsFiles = 'assets/**/*.js',
    jsDest = 'static/';



gulp.task('css', function(){
        gulp.src('assets/**/*.css')
            .pipe(order(['bootsrap/*', '**/*']))
            .pipe(minifyCSS())
            .pipe(concat('styles.min.css'))
            .pipe(gulp.dest(jsDest))
});

gulp.task('scripts', function() {
    return gulp.src(jsFiles)

        .pipe(concat('scripts.js'))
        .pipe(gulp.dest(jsDest))
        .pipe(rename('scripts.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(jsDest));

});

gulp.task('default',['css', 'scripts']);


