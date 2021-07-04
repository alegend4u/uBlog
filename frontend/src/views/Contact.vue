<template>
  <div class="split">
    <div class="contact_info">
      <p class="header_text">Let's Connect</p>
      <p class="subtitle_text">
        ...always open for ideas, suggestions, opinions
      </p>
      <div class="page_body">
        <div class="quote">
          <p class="quote_text">"You cannot not communicate."</p>
          <p class="author">- Paul Watzlawick</p>
        </div>
        <form class="feedback_form" method="post">
          <input type="text" name="name" placeholder="Name" />
          <input type="text" name="email" placeholder="Email" required />
          <textarea
            name="feedback"
            rows="5"
            required
            placeholder="Any idea, feedback, suggestion, greeting or even your fav music."
          ></textarea>
          <input type="submit" class="submit_button" />
        </form>
      </div>
      <div class="social_media">
        <a
          href="https://www.instagram.com/_a.legend_/"
          target="_blank"
          class="fab fa-instagram"
          ><font-awesome-icon :icon="['fab', 'instagram']" />
        </a>
        <a
          href="https://www.linkedin.com/in/rishabh-prajapati0/"
          target="_blank"
          class="fab fa-linkedin"
          ><font-awesome-icon :icon="['fab', 'linkedin']" />
        </a>
        <a
          href="https://github.com/alegend4u/"
          target="_blank"
          class="fab fa-github"
          ><font-awesome-icon :icon="['fab', 'github']"
        /></a>

        <!-- <a
          href="mailto:rishabh.prajapati0@gmail.com"
          target="_blank"
          class="fas fa-at"
        >
        </a>

        <a
          href="tel:+91942-928-8602"
          target="_blank"
          class="fas fa-phone-square-alt"
        ></a> -->
      </div>
      <div class="email_phone">
        <a class="email" href="mailto:rishabh.prajapati0@gmail.com"
          >rishabh.prajapati0@gmail.com</a
        >
        <a class="phone" href="tel:+91942-928-8602">+91 942-928-8602</a>
      </div>
    </div>
    <img
      src="../assets/portfolio/contact_image.jpeg"
      alt="My another image here."
    />
  </div>
</template>

<style lang="scss" scoped>
@import "@/sass/portfolio/contact.sass";
</style>
