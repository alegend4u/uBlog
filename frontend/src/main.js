import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import { faFontAwesome } from "@fortawesome/free-brands-svg-icons";

library.add(faGithub);
library.add(faFontAwesome);

createApp(App).use(router).mount("#app");
