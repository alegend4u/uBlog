const path = require("path")

const pages = {
  index: "src/main.js",
}

module.exports = {
  // publicPath: "/static/vue/",
  outputDir: "./build/static/vue/",
  indexPath: "../../templates/vue_index.html",

  pages: pages,
  css: {
    loaderOptions: {
      sass: {
        sassOptions: {
          // indentedSyntax: true,
          // includePaths: [path.resolve(__dirname, "./sass")],
          // additionalData: `@import "@/sass/main.sass"`,
        },
      },
    },
  },
}
