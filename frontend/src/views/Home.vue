<template>
  <nav class="nav">
    <div class="menu-btn">
      <span class="burger upper"></span>
      <span class="burger middle"></span>
      <span class="burger lower"></span>
    </div>
    <a class="title" href="/">Rishabh Prajapati</a>
    <ul class="navbar">
      <li><a class="navbar__item" href="/">About Me</a></li>
      <li><a class="navbar__item" href="/portfolio">Portfolio</a></li>
      <li><a class="navbar__item" href="/timeline">Timeline Blog</a></li>
      <li><a class="navbar__item" href="/contact">Contact Me</a></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Home",
}
</script>

<style lang="scss">
@import "@/sass/main.sass";
</style>
