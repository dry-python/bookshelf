from dependencies import Injector
from dependencies import Package


django = Package("django")

services = Package("bookshelf.services")
repositories = Package("bookshelf.repositories")
functions = Package("bookshelf.functions")


class ShowPrices(Injector):

    show_prices = services.ShopCategoryPrices.show
    load_category = repositories.load_category
    load_prices = repositories.prices_for_category
    instantiate_forms = functions.make_subscription_forms


class BuySubscription(Injector):

    buy_subscription = services.BuySubscription.buy
    load_category = repositories.load_category
    load_price = repositories.load_price
    load_profile = repositories.load_profile
    decrease_balance = repositories.decrease_balance
    save_profile = repositories.save_profile
    current_date = django.utils.timezone.now
    create_subscription = repositories.create_subscription
    send_notification = functions.SendNotification.do
    messages = functions.Messages
    create_notification = repositories.create_notification


class ShowCategory(Injector):

    show = services.ShowCategory.show
    load_category = repositories.load_category
    load_subscription = repositories.load_subscription
    load_entries = repositories.load_entries


class ListCategories(Injector):

    list = services.ListCategories.list
    load_categories = repositories.load_categories
    keep_subscriptions = repositories.category.keep_subscribed


class CategoriesForPurchase(Injector):

    list = services.CategoriesForPurchase.list
    load_categories = repositories.load_categories
    exclude_subscriptions = repositories.category.exclude_subscribed
    filter_prices = repositories.category.keep_with_prices
    load_prices = repositories.cheapest_price_by_category


class ListNotifications(Injector):

    list = services.ListNotifications.list
    load_notifications = repositories.load_notifications


class ShowProfile(Injector):

    show = services.ShowProfile.show
    load_profile = repositories.load_profile


class PutMoneyIntoAccount(Injector):

    put = services.PutMoneyIntoAccount.put
    load_profile = repositories.load_profile
    add_balance = repositories.add_balance
    save_profile = repositories.save_profile
    send_notification = functions.SendNotification.do
    messages = functions.Messages
    create_notification = repositories.create_notification


class SignUp(Injector):

    register_user = services.SignUp.register_user
    validate_password = functions.validate_password
    create_user = repositories.create_user
    save_password = repositories.save_password
    create_profile = repositories.create_profile
    store_user_in_session = django.contrib.auth.login
    send_notification = functions.SendNotification.do
    messages = functions.Messages
    create_notification = repositories.create_notification
