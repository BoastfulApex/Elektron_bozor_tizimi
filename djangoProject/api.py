from rest_framework import routers
from Store.views import *
from employee.views import *
from moderator.views import *
router = routers.DefaultRouter()
router.register(r'customer', CustomerView,basename='customer')
router.register(r'category', CategoriesView,basename='category')
router.register(r'product', ProductsView,basename='product')
router.register(r'product_by_category', ProductByCategoryView,basename='product_by_category')
router.register(r'order', OrdersView,basename='order')
router.register(r'order_details', OrderDetailsView,basename='order_details')
router.register(r'order_details_action', OrderDetailsActionsView,basename='order_details_action')
router.register(r'employee', EmployeeView,basename='employee')
router.register(r'moderator', ModeratorView,basename='moderator')
