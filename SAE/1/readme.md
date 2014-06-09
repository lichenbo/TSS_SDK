NJU Software Institute TSS REST API v1.0
=======

###获取指定课程的通知列表 `GET /api/v1.0/course/:courseid/announcement`
返回信息有：

 - `announce_title` 通知标题
 - `announce_text` 通知正文
 - `announce_date` 通知日期

如：`GET http://njutss.sinaapp.com/api/v1.0/course/c0863/announcement`

###获取指定课程的作业列表 `GET /api/v1.0/course/:courseid/assignment`

返回信息有：

 - `due_date` 截止日期
 - `assignment_number` 作业编号
 - `escription` 作业说明

如：`GET http://njutss.sinaapp.com/api/v1.0/course/c0863/assignment`

###获取指定用户的课程列表 `POST /api/v1.0/user/:username/courselist`

需要POST提交的信息：

 - `password` 指定用户的密码

返回信息有：

 - `course_id` 课程编号
 - `update_time` 最后更新时间
 - `course_name` 课程名称
 - `teacher` 任课教师

如：`POST http://njutss.sinaapp.com/api/v1.0/user/lcb11/courselist`
