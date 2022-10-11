
import { onMounted, watch } from '@vue/runtime-core';
import axios from "axios";
export default function getArticleDate(info,route) {
        const getData = async () => {
            let url = "/api/article";
            let parms = new URLSearchParams();
            parms.appendIfExists("page", route.query.page);
            parms.appendIfExists("search", route.query.search);
            const parmsString = parms.toString();
            if (parmsString.charAt(0) !== "") {
              url += "/?" + parmsString;
            }
            const response = await axios.get(url);
            info.value = response.data;
               
          };
      
          onMounted(getData);
          watch(route,getData);
}