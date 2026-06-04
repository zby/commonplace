// Attach click-to-sort to every rendered table. Progressive enhancement only:
// the markdown stays a plain GFM table; sorting appears in the MkDocs HTML build.
// Loaded via extra_javascript in mkdocs.yml (after tablesort.min.js).
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("table").forEach(function (table) {
    new Tablesort(table);
  });
});
