#导入时间模块
import time
from time  import sleep
import slide
# # 点击好友微聊
# driver.find_element_by_xpath("//android.widget.TextView[@text='待机测试']").click()
# sleep(2)
# # 点击进入好友微聊界面后点表情
# driver.find_element_by_accessibility_id('双击切换至表情').click()
# sleep(2)
# # 层级定位表情
# # element = driver.find_element_by_id("com.xtc.watch:id/vp_show_exp")
# # element.find_element_by_class_name("android.view.ViewGroup").click()
#
# #循环发送3个表情
# a = 1
# while a < 4:
#     element = driver.find_element_by_class_name('androidx.viewpager.widget.ViewPager')
#     elements = element.find_elements_by_class_name('android.widget.ImageView')
#     elements[3].click()
#     sleep(3)
#     a = a+1
# sleep(5)
# # 点击返回到微聊界面
# driver.find_element_by_accessibility_id('返回').click()
# sleep(2)
# # 使用android——uiautomator定位，new UiSelector()中间要有空格，并且最外层要使用单引号，里面使用双引号。否则会报错
# driver.find_element_by_android_uiautomator('new UiSelector().text("更多")').click()
# sleep(5)
# # 点击定位按钮
# driver.find_element_by_id('com.xtc.watch:id/lottieAnimationLocation').click()
# sleep(63)
# # 点击更新位置按钮
# driver.find_element_by_id('com.xtc.watch:id/iv_refresh_location').click()
# sleep(10)
# # 点击微聊
# driver.find_element_by_id('com.xtc.watch:id/lottieAnimationChat').click()
# sleep(10)
# 点击进入更多列表界面
slide.remote_connection.find_element_by_id("com.xtc.watch:id/lottieAnimationMore")
slide.swipeDown(slide.remote_connection)

# 退出APP
slide.remote_connection.quit()