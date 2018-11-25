from dependencies import Injector, Package


django = Package("django")

services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


class ShowPrices(Injector):

    show_prices = services.ShopCategoryPrices.show

    class impl(Injector):

        load_category = repositories.load_category
        load_prices = repositories.prices_for_category
        instantiate_forms = functions.make_subscription_forms


class BuySubscription(Injector):

    buy_subscription = services.BuySubscription.buy

    class impl(Injector):

        load_category = repositories.load_category
        load_price = repositories.load_price
        load_profile = repositories.load_profile
        decrease_balance = repositories.decrease_balance
        save_profile = repositories.save_profile
        calculate_period = functions.calculate_period
        create_subscription = repositories.create_subscription
        send_notification = functions.SendNotification.do
        messages = functions.Messages
        create_notification = repositories.create_notification


class ShowCategory(Injector):

    show = services.ShowCategory.show

    class impl(Injector):

        load_category = repositories.load_category
        load_subscription = repositories.load_subscription
        load_entries = repositories.load_entries


class ListCategories(Injector):

    list = services.ListCategories.list

    class impl(Injector):

        load_categories = repositories.load_categories
        keep_subscriptions = repositories.category.keep_subscribed


class CategoriesForPurchase(Injector):

    list = services.CategoriesForPurchase.list

    class impl(Injector):

        load_categories = repositories.load_categories
        exclude_subscriptions = repositories.category.exclude_subscribed
        filter_prices = repositories.category.keep_with_prices
        load_prices = repositories.cheapest_price_by_category


class ListNotifications(Injector):

    list = services.ListNotifications.list

    class impl(Injector):

        load_notifications = repositories.load_notifications


class ShowProfile(Injector):

    show = services.ShowProfile.show

    class impl(Injector):

        load_profile = repositories.load_profile


class PutMoneyIntoAccount:

    put = services.PutMoneyIntoAccount.put

    class impl(Injector):

        load_profile = repositories.load_profile
        add_balance = repositories.add_balance
        save_profile = repositories.save_profile
        send_notification = functions.SendNotification.do
        messages = functions.Messages
        create_notification = repositories.create_notification


class SignUp(Injector):

    register_user = services.SignUp.register_user

    class impl(Injector):

        validate_password = functions.validate_password
        create_user = repositories.create_user
        save_password = repositories.save_password
        create_profile = repositories.create_profile
        store_user_in_session = django.contrib.auth.login
        send_notification = functions.SendNotification.do
        messages = functions.Messages
        create_notification = repositories.create_notification
