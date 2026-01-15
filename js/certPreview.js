// 测试：验证文件是否成功加载
console.log("certPreview.js 已加载，开始初始化证书预览功能");

// 等待DOM完全加载后再执行代码（避免元素未渲染导致获取失败）
document.addEventListener('DOMContentLoaded', function() {
    // 获取弹窗、关闭按钮、加载器、图片元素（添加容错）
    const modal = document.getElementById("certModal");
    const closeBtn = document.querySelector(".close-modal");
    const loader = document.getElementById("loader");
    const modalImg = document.getElementById("modalImg");

    // 检测关键元素是否存在，避免报错
    if (!modal || !closeBtn || !loader || !modalImg) {
        console.error("证书预览弹窗的关键元素未找到，请检查HTML结构中的ID/类名是否正确");
        return;
    }

    // 给所有预览按钮绑定点击事件
    const previewBtns = document.querySelectorAll('.cert-preview');
    if (previewBtns.length === 0) {
        console.warn("未找到带有 .cert-preview 类的预览按钮");
    }

    previewBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault(); // 阻止a标签默认跳转
            // 核心修正：把block改成flex，确保弹窗居中显示
            modal.style.display = "flex"; 
            loader.style.display = "block"; // 显示加载器
            modalImg.style.display = "none"; // 先隐藏图片

            const imgSrc = this.getAttribute('data-img'); // 获取图片路径
            if (!imgSrc) {
                console.error("预览按钮缺少 data-img 属性");
                loader.style.display = "none";
                modalImg.alt = "No image path provided";
                modalImg.style.display = "block";
                return;
            }

            modalImg.src = imgSrc; // 设置图片地址

            // 图片加载完成后隐藏加载器、显示图片
            modalImg.onload = function() {
                loader.style.display = "none";
                modalImg.style.display = "block";
                console.log(`图片加载成功: ${imgSrc}`);
            };

            // 图片加载失败时提示
            modalImg.onerror = function() {
                loader.style.display = "none";
                modalImg.alt = "Certificate image not found";
                modalImg.style.display = "block";
                console.error(`图片加载失败: ${imgSrc}，请检查路径是否正确`);
            };
        });
    });

    // 优化关闭按钮逻辑（增加事件冒泡阻止）
    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.stopPropagation(); // 阻止事件冒泡到弹窗
            modal.style.display = "none";
        });
    }

    // 优化点击弹窗背景关闭逻辑
    modal.addEventListener('click', function(e) {
        // 确保点击的是弹窗背景而非内容
        if (e.target === modal || e.target.classList.contains('modal')) {
            modal.style.display = "none";
        }
    });

    // 优化ESC键关闭逻辑
    document.addEventListener('keydown', function(e) {
        if (e.key === "Escape" && modal.style.display !== "none") {
            modal.style.display = "none";
        }
    });

    console.log("证书预览功能初始化完成");
});

