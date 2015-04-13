module.exports = function(grunt) {

    // Configure task(s)
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            build: {
                files: {
                    'static/js/script-min.js': ['static/src/js/*.js'],
                    'static/lib/lib-min.js':['static/src/lib/*.js']
                }
            },
            dev: {
                options: {
                    beautify: true,
                    mangle: false,
                    compress: false,
                    preserveComments: 'all'
                },
                files: {
                    'static/js/script-min.js': ['static/src/js/*.js'],
                    'static/lib/lib-min.js':['static/src/lib/*.js']
                }
            }
        },
        sass: {
            dev: {
                options: {
                    outputStyle: 'expanded'
                },
                files: {
                    'static/css/style.css': 'static/src/css/main.scss'
                }
            },
            build: {
                options: {
                    outputStyle: 'compressed'
                },
                files: {
                    'static/css/style.css': 'static/src/css/main.scss'
                }
            }
        },
        watch: {
            js: {
                files: ['static/src/js/*.js'],
                tasks: ['uglify:dev']
            },
            css: {
                files: ['static/src/css/**/*.scss'],
                tasks: ['sass:dev']
            }
        }
    });

    // Load the plugin
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-sass');

    // Register task(s)
    grunt.registerTask('default', ['uglify:dev', 'sass:dev']);
    grunt.registerTask('build', ['uglify:build', 'sass:build']);

};
