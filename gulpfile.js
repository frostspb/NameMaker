let gulp = require('gulp');
let concat = require('gulp-concat');
let cleanCSS = require('gulp-clean-css');
let rename = require('gulp-rename');
let uglify = require('gulp-uglify');
let order = require('gulp-order');

let jsFiles = 'assets/**/*.js',
    jsDest = 'static/';



gulp.task('css', function(done){
        gulp.src('assets/**/*.css')
            .pipe(order(['bootsrap/*', '**/*']))
            .pipe(cleanCSS({compatibility: 'ie8'}))
            .pipe(concat('styles.min.css'))
            .pipe(gulp.dest(jsDest))
        done()
});

gulp.task('scripts', function(done) {
    return gulp.src(jsFiles)

        .pipe(concat('scripts.js'))
        .pipe(gulp.dest(jsDest))
        .pipe(rename('scripts.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(jsDest));
        done()

});

gulp.task('default',gulp.series('css', 'scripts'));


