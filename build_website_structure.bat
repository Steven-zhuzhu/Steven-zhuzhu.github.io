@echo off
chcp 65001 > nul  :: 解决中文乱码问题
cls  :: 清空命令行窗口，显示更整洁

:: ==============================================
:: 第一步：创建所有网站文件夹（无拼写错误）
:: ==============================================
echo 🚀 正在创建网站文件夹...
mkdir home
mkdir about
mkdir achievements\competition-awards
mkdir achievements\academic-awards
mkdir achievements\others
mkdir quantum-projects\project-1-particle-in-box
mkdir quantum-projects\project-2-quantum-tunneling
mkdir quantum-projects\coding
mkdir climate-modeling-project\introduction
mkdir climate-modeling-project\literature-review
mkdir climate-modeling-project\math-model
mkdir climate-modeling-project\coding
mkdir concord-coding-apps\introduction
mkdir concord-coding-apps\coding
mkdir concord-coding-apps\web
mkdir my-favorite-books\why-books
mkdir extracurricular-activities\my-school-club\astronomy-club
mkdir extracurricular-activities\my-school-club\physics-club
mkdir extracurricular-activities\my-school-club\badminton-club
mkdir extracurricular-activities\my-reading-club
mkdir my-leisure-hobbies\violin
mkdir my-leisure-hobbies\minecraft
mkdir my-leisure-hobbies\starry
mkdir contact
echo ✅ 文件夹创建完成！

:: ==============================================
:: 第二步：创建所有空HTML文件（按板块分类）
:: ==============================================
echo 📄 正在创建空HTML文件...

:: 【基础板块】
echo. > home\index.html
echo. > about\about.html
echo. > contact\index.html

:: 【成果展示板块】
echo. > achievements\achievements.html
echo. > achievements\competition-awards\competition-awards.html
echo. > achievements\academic-awards\academic-awards.html
echo. > achievements\others\others.html

:: 【量子项目板块】
echo. > quantum-projects\quantum-overview.html
echo. > quantum-projects\project-1-particle-in-box\project1.html
echo. > quantum-projects\project-2-quantum-tunneling\project2.html
echo. > quantum-projects\coding\coding.html

:: 【气候建模板块】
echo. > climate-modeling-project\climate.html
echo. > climate-modeling-project\introduction\introduction.html
echo. > climate-modeling-project\literature-review\review.html
echo. > climate-modeling-project\math-model\mathematic-model.html
echo. > climate-modeling-project\coding\coding.html

:: 【编码应用板块】
echo. > concord-coding-apps\Apps.html
echo. > concord-coding-apps\introduction\introduction.html
echo. > concord-coding-apps\coding\coding.html
echo. > concord-coding-apps\web\web.html

:: 【书籍板块】
echo. > my-favorite-books\my-books.html
echo. > my-favorite-books\why-books\why-books.html

:: 【课外活动板块】
echo. > extracurricular-activities\activities.html
echo. > extracurricular-activities\my-school-club\my-school-club.html
echo. > extracurricular-activities\my-school-club\astronomy-club\astronomy-club.html
echo. > extracurricular-activities\my-school-club\physics-club\physics-club.html
echo. > extracurricular-activities\my-school-club\badminton-club\badminton-club.html
echo. > extracurricular-activities\my-reading-club\reading.html

:: 【休闲爱好板块】
echo. > my-leisure-hobbies\hobbies.html
echo. > my-leisure-hobbies\violin\violin.html
echo. > my-leisure-hobbies\minecraft\minecraft.html
echo. > my-leisure-hobbies\starry\starry.html

:: ==============================================
:: 第三步：提示完成
:: ==============================================
echo ✅ 所有空HTML文件创建完成！
echo ==============================================
echo 🎉 网站基础结构搭建完毕！
echo 📂 已创建：所有文件夹 + 32个空HTML文件
echo 📌 接下来你只需：
echo    1. 打开每个HTML文件，填充自己的内容（比如个人介绍、项目描述）
echo    2. 补充CSS/JS样式，让网站更美观
echo ==============================================
pause