const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app){
    app.use(
        '/bus',
        createProxyMiddleware({
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            
        })
    ),
    app.use(
        '/temp',
        createProxyMiddleware({
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            
        })
    ),
    app.use(
        '/rain',
        createProxyMiddleware({
            target: 'http://127.0.0.1:5000',
            changeOrigin: true,
            
        })
    ),
    app.use(
        '/tts',
        createProxyMiddleware({
            target: 'http://172.20.10.6:5003',
            changeOrigin: true,      
        })
    );
};