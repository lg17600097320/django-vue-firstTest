import axios from "axios";
 async function authorization() {
    const storage = localStorage;

    let hasLogin = false;
    let  username = storage.getItem('username.myblog');

    const expiredTime = Number(storage.getItem('expiredTime.myblog'));
    const cuurent = (new Date()).getTime();
    const refreshToken = storage.getItem('refresh.myblog');

    //初始token未过期
    if(expiredTime > cuurent){
        hasLogin = true;
        console.log('authorization access');
    }
    //初始token过期
    //申请刷新token
    else if( refreshToken !== null ){
        try {
            let response = await axios.post('/api/token/refresh/',{
                'refresh': refreshToken
            }) ;
            const nextExpiredTime = Date.parse(response.headers.date) + 60000;

            storage.setItem('access.myblog',response.data.access);
            storage.setItem('expiredTime',nextExpiredTime);
            storage.removeItem('refresh.myblog');

            hasLogin = true;

            console.log('authorization refresh');
        } catch (error) {
            storage.clear();
            hasLogin = false;
            console.log(' authorization err');
        }
    }
    else{
        storage.clear();
        hasLogin = false;
        console.log(' authorization exp');
    }
    console.log('authorization done')
    return [hasLogin,username]
 }

 export default authorization;