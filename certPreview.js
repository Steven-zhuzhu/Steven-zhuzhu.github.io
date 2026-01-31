// 验证文件加载
console.log("certPreview.js 已加载，开始初始化证书预览功能");

// 等待DOM完全加载
document.addEventListener('DOMContentLoaded', function() {
    // 获取核心元素（容错处理）
    const modal = document.getElementById("certModal");
    const closeBtn = document.querySelector(".close-modal");
    const loader = document.getElementById("loader");
    const modalImg = document.getElementById("modalImg");

    // 检测关键元素是否存在
    if (!modal || !closeBtn || !loader || !modalImg) {
        console.error("证书预览弹窗的关键元素未找到，请检查HTML结构中的ID/类名");
        return;
    }

    // 绑定所有预览按钮点击事件
    const previewBtns = document.querySelectorAll('.cert-preview');
    if (previewBtns.length === 0) {
        console.warn("未找到带有 .cert-preview 类的预览按钮");
    }

    previewBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault(); // 阻止a标签默认跳转
            
            // 显示弹窗和加载器，隐藏图片
            modal.style.display = "flex"; 
            loader.style.display = "block"; 
            modalImg.style.display = "none"; 

            // 获取图片路径
            const imgSrc = this.getAttribute('data-img');
            if (!imgSrc) {
                console.error("预览按钮缺少 data-img 属性");
                loader.style.display = "none";
                modalImg.alt = "No image path provided";
                modalImg.style.display = "block";
                return;
            }

            // 设置图片地址并处理加载状态
            modalImg.src = imgSrc;
            modalImg.onload = function() {
                loader.style.display = "none";
                modalImg.style.display = "block";
                console.log(`图片加载成功: ${imgSrc}`);
            };
            modalImg.onerror = function() {
                loader.style.display = "none";
                modalImg.alt = "Certificate image not found";
                modalImg.style.display = "block";
                console.error(`图片加载失败: ${imgSrc}，请检查路径是否正确`);
            };
        });
    });

    // 关闭按钮事件（阻止冒泡）
    closeBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        modal.style.display = "none";
        // 重置图片，避免下次打开显示旧图
        modalImg.src = "";
        modalImg.alt = "";
    });

    // 点击弹窗外区域关闭
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = "none";
            modalImg.src = "";
            modalImg.alt = "";
        }
    });

    // 键盘ESC关闭弹窗
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === "flex") {
            modal.style.display = "none";
            modalImg.src = "";
            modalImg.alt = "";
        }
    });

    // 初始化弹窗DOM（如果HTML中未定义则自动创建）
    if (!document.getElementById("certModal")) {
        const modalContainer = document.createElement("div");
        modalContainer.id = "certModal";
        modalContainer.className = "modal";
        modalContainer.innerHTML = `
            <div class="modal-content">
                <span class="close-modal">&times;</span>
                <div class="loader" id="loader"></div>
                <img class="modal-img" id="modalImg">
            </div>
        `;
        document.body.appendChild(modalContainer);
        console.log("自动创建证书预览弹窗DOM结构");
    }
});