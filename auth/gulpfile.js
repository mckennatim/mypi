var gulp = require('gulp');
var traceur = require('gulp-traceur');
var webserver =require('gulp-webserver');
var watch =require('gulp-watch');
 
gulp.task('default', function () {
    return gulp.src('src/*.js')
    	.pipe(watch('src/*.js'))
        .pipe(traceur())
        .pipe(gulp.dest('dist'));
});

gulp.task('www', function(){
	gulp.src('dist')
		.pipe(webserver({
			fallback: 'index.html',
			host: '10.0.1.154',
			port: 8005,
			livereload: true
	}));	
})