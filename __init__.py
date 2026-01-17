# # import os
# # import sys
# # import django

# # # Setup Django environment
# # sys.path.append(r'E:/School_custom/core')  # Add your Django project directory to the Python path
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # Use the correct settings module
# # django.setup()

# # from rest_framework_simplejwt.tokens import AccessToken


# # token = AccessToken('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMjAwMDk1LCJpYXQiOjE3NDAxOTg5OTksImp0aSI6ImY1MmU4MTA1MzNiZjRlODA5YmNhMTJmMGIxYWI2ZDU4IiwidXNlcl9pZCI6MX0.Ul9fN_ZeX1iUGy8ozmvJ5Oe873Ej6fWyOiO7RfjpICM"')
# # print(token.payload)
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLabel
# )
# from PySide6.QtCore import (
#     QPropertyAnimation, QEasingCurve, QRect, QParallelAnimationGroup, Qt
# )

# class SlideStack(QStackedWidget):
#     def __init__(self):
#         super().__init__()
#         self.animation_duration = 400
#         self._anim_group = None

#     def slide_to_index(self, next_index):
#         if next_index == self.currentIndex():
#             return

#         current_index = self.currentIndex()
#         current_widget = self.currentWidget()
#         next_widget = self.widget(next_index)

#         width = self.frameRect().width()
#         height = self.frameRect().height()

#         # Устанавливаем начальное положение следующего виджета
#         next_widget.setGeometry(width, 0, width, height)
#         next_widget.show()

#         # Анимация текущего виджета — уходит влево
#         anim_current = QPropertyAnimation(current_widget, b"geometry")
#         anim_current.setDuration(self.animation_duration)
#         anim_current.setStartValue(QRect(0, 0, width, height))
#         anim_current.setEndValue(QRect(-width, 0, width, height))
#         anim_current.setEasingCurve(QEasingCurve.InOutQuad)

#         # Анимация следующего виджета — заходит справа
#         anim_next = QPropertyAnimation(next_widget, b"geometry")
#         anim_next.setDuration(self.animation_duration)
#         anim_next.setStartValue(QRect(width, 0, width, height))
#         anim_next.setEndValue(QRect(0, 0, width, height))
#         anim_next.setEasingCurve(QEasingCurve.InOutQuad)

#         # Группируем анимации
#         self._anim_group = QParallelAnimationGroup()
#         self._anim_group.addAnimation(anim_current)
#         self._anim_group.addAnimation(anim_next)

#         # После завершения — переключаем экран и сбрасываем геометрию
#         def on_finished():
#             self.setCurrentIndex(next_index)
#             current_widget.setGeometry(0, 0, width, height)
#             next_widget.setGeometry(0, 0, width, height)

#         self._anim_group.finished.connect(on_finished)
#         self._anim_group.start()

# class Screen(QWidget):
#     def __init__(self, name, go_next=None):
#         super().__init__()
#         layout = QVBoxLayout()
#         label = QLabel(name)
#         label.setAlignment(Qt.AlignCenter)
#         label.setStyleSheet("font-size: 24px;")
#         layout.addWidget(label)
#         if go_next:
#             btn = QPushButton("Перейти")
#             btn.clicked.connect(go_next)
#             layout.addWidget(btn)
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication([])

#     stack = SlideStack()

#     screen1 = Screen("Экран 1", lambda: stack.slide_to_index(1))
#     screen2 = Screen("Экран 2", lambda: stack.slide_to_index(0))

#     stack.addWidget(screen1)
#     stack.addWidget(screen2)

#     stack.resize(400, 300)
#     stack.show()

#     app.exec()

