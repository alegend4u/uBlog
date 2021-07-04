<template>
  <div class="section" id="section_motivation">
    <div class="banner">My Motivation</div>
    <div class="container" id="motivation">
      <p>
        It's just that I don't want to die regretting that I could've tried that
        and It could have been more fun living life.<br />
        It's just that what incredible things I can do if I consider myself
        fearless.<br />
        It's just that I want to jump on the opportunities I get. <br />
        It's just that I truly want to know my real limits. <br />
        It's just that I want to LIVE the process, the journey of getting what I
        want to be. <br />
      </p>
      <img src="../assets/portfolio/me.png" alt="Me" />
    </div>
  </div>
  <div class="section">
    <div class="banner">Projects</div>
    <div class="container" id="projects">
      <div class="project" id="project_music">
        <img
          src="../assets/portfolio/music.png"
          alt="Music Recommendation System"
        />
        <p class="title">Better Waves</p>
      </div>
      <div class="project" id="project_uit">
        <img src="../assets/portfolio/unifiedit.jpg" alt="UnifiedIT" />
        <p class="title">UnifiedIT</p>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="banner">Experience</div>
    <div class="container" id="experience">
      <div class="container__item">
        <div class="flex">
          <p class="title">Software Engineer - Core Platform</p>
          <p class="duration">September 2020 - Present</p>
        </div>
      </div>
      <p class="container__item__subtitle">Soroco India Pvt. Ltd.</p>
      <p class="container__item_description"></p>
      <div class="container__item">
        <div class="flex">
          <p class="title">Programmer Analyst - AI Department</p>
          <p class="duration">December 2019 - September 2020</p>
        </div>
        <p class="container__item__subtitle">
          Dosepack LLP, Meditab Softwares Inc., India
        </p>
        <div class="container__item__description">
          <ul>
            <li>
              Camera Module
              <ul>
                <li>
                  For a machine vision camera, I implemented a stable Python API
                  that uses SDK provided in C and solved the challenge of
                  converting the memory block of raw image to the NumPy matrix
                  without image distortion.
                </li>
                <li>
                  Solved the challenge of parallelization and synchronization
                  (0.1s of difference between any two frames’ time stamps) of
                  capturing frames when multiprocessing more than one module.
                </li>
              </ul>
            </li>
            <li>
              Face Module
              <ul>
                <li>
                  Developed a merging algorithm for tracks between two camera
                  modules which uses the fundamental matrix between the same.
                </li>
                <li>
                  Designed a solution for filtering unwanted tracks which are
                  determined by the nature of values of the first and
                  second-order derivatives of the series of heights of the
                  subsequent face detections.
                </li>
                <li>
                  Developed a merging algorithm for tracks between two camera
                  modules which uses the fundamental matrix between the same.
                </li>
                <li>
                  Restructured the codebase into a loose-coupled and
                  high-cohesive one and achieved a more concise and highly
                  pluggable code. Algorithmic optimizations in terms of time and
                  memory and improvement in the real-time operation.
                </li>
                <li>
                  Developed a sync mechanism between the Google Cloud Bucket and
                  the local file system which is to be used in real-time.
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
      <div class="container__item">
        <div class="flex">
          <p class="title">Full Stack Developer Summer Intern</p>
          <p class="duration">May 2018 - July 2018</p>
        </div>
        <p class="container__item__subtitle">
          Limelight Innovations, Ahmedabad
        </p>
        <div class="container__item__description">
          <ul>
            <li>Improved the overall functioning and fixed bugs.</li>
            <li>Tech. Stack: Django, RethinkDB, PostgreSQL, MQTT, Docker.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="banner">Education</div>
    <div class="container" id="education">
      <div class="container__item">
        <div class="flex">
          <p class="title">
            Faculty of Technology, Dharmsinh Desai University, Nadiad
          </p>
          <p class="duration">July 2016 - May 2020</p>
        </div>
        <p class="container__item__subtitle">Bachelor of Technology</p>
        <p>Course: Information Technology</p>
      </div>
      <div class="container__item">
        <div class="flex">
          <p class="title">Smt. M. M. Mehta English Medium School</p>
        </div>
        <p>Palanpur, India</p>
      </div>
    </div>
  </div>
  <div class="scroll_buttons">
    <div class="scroll_btn"><i class="arrow up"></i></div>
    <div class="scroll_btn"><i class="arrow down"></i></div>
  </div>

  {# Modals #}
  <div class="modal" id="modal-music">
    <div class="modal-content">
      <div class="modal-header">
        Better Waves - Music Recommendation System<span class="close"
          >&times;</span
        >
      </div>
      <div class="modal-body">
        <div class="description">
          <p>
            Lorem ipsum Lorem ipsumLorem ipsumLorem ipsumLorem ipsum Lorem
            ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem
            ipsumLorem ipsumLorem ipsum Lorem ipsum Lorem ipsumLorem ipsumLorem
            ipsumLorem ipsumLorem ipsumLorem ipsum Lorem ipsumLorem ipsumLorem
            ipsumLorem ipsumLorem ipsum Lorem ipsumLorem ipsum
          </p>
          <div class="github_link">
            <a
              class="fab fa-github"
              target="_blank"
              href="https://github.com/alegend4u/better-waves"
              ><font-awesome-icon icon="github"
            /></a>
          </div>
        </div>
        <div class="project_gallery"></div>
      </div>
    </div>
  </div>
  <div class="modal" id="modal-uit">
    <div class="modal-content">
      <span class="close">&times;</span>
      Put unifiedit content here.
    </div>
  </div>

  <!-- TODO: change pure js to vue js code. -->
  <!-- <script src="{% static 'portfolio/js/portfolio.js' %}"></script> -->
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "@/sass/portfolio/portfolio.sass";
</style>
