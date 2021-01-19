"use strict";

$(".btnBegin").on("click", function () {
  location.href = "learn/";
});
$(document).ready(function () {
  $html = preg_replace('#<script(.*?)>(.*?)</script>#is', '', $html);
});