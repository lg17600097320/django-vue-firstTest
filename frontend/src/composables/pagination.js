
// 这是一个分页的组件,包含三个方法
// 分别是 
// is_page_exists(info,direction)   判断是否存在分页
// get_page_param (info,route,direction)  判断是否存在上页和下页
// get_path (info,direction)    得到页码


export default function pagination(info,route){

    const isPageExists = (direction) => {
        return is_page_exists(info,direction)
    }

    const  getPageParam = (direction) => {
        return get_page_param (info,route,direction)
    }

    const getPath = (direction) => { 
            return get_path (info,direction)
    }   

    return {
        isPageExists,
        getPageParam,
        getPath
    }
}
 // 判断页面是否存在
 function is_page_exists(info,direction) {
    if (direction == "next") {
      return info.value.next !== null;
    }
    return info.value.previous !== null;
  }
  // 获取页码
  function get_page_param (info,route,direction) {
    try {
      let url_string;
      switch (direction) {
        case "next":
          url_string = info.value.next;
          break;
        case "previous":
          url_string = info.value.previous;
          break;
        default:
          return route.query.page;
      }
      const url = new URL(url_string);
      return url.searchParams.get("page");
    } catch (err) {
      return;
    }
  }
// 获取下一页
function get_path (info,direction) {
    let url = "";
    try {
      switch (direction) {
        case "next":
          if (info.value.next !== undefined) {
            url += new URL(info.value.next).search;
          }
          break;
        case "previous":
          if (info.value.previous !== undefined) {
            url += new URL(info.value.previous).search;
          }
          break;
      }
    } catch (error) {
      return error;
    }
    return url;
  }