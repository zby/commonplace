// Inject Giscus after the rendered page body. Keeping this as a site asset avoids
// taking over the ProperDocs theme template for one widget.
document.addEventListener("DOMContentLoaded", function () {
  var main = document.querySelector('[role="main"]');

  if (!main || document.querySelector(".giscus-comments")) {
    return;
  }

  var section = document.createElement("section");
  section.className = "giscus-comments";
  section.setAttribute("aria-labelledby", "giscus-comments-heading");

  var heading = document.createElement("h2");
  heading.id = "giscus-comments-heading";
  heading.textContent = "Comments";

  var container = document.createElement("div");
  container.className = "giscus";

  var script = document.createElement("script");
  script.src = "https://giscus.app/client.js";
  script.setAttribute("data-repo", "zby/commonplace");
  script.setAttribute("data-repo-id", "R_kgDORahwHw");
  script.setAttribute("data-category", "Announcements");
  script.setAttribute("data-category-id", "DIC_kwDORahwH84DBTSV");
  script.setAttribute("data-mapping", "pathname");
  script.setAttribute("data-strict", "1");
  script.setAttribute("data-reactions-enabled", "1");
  script.setAttribute("data-emit-metadata", "0");
  script.setAttribute("data-input-position", "bottom");
  script.setAttribute("data-theme", "preferred_color_scheme");
  script.setAttribute("data-lang", "en");
  script.setAttribute("data-loading", "lazy");
  script.setAttribute("crossorigin", "anonymous");
  script.async = true;

  section.appendChild(heading);
  section.appendChild(container);
  container.appendChild(script);
  main.appendChild(section);
});
