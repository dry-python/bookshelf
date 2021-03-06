from dependencies import Injector
from dependencies import Package


django = Package("django")

usecases = Package("bookshelf.usecases")
repositories = Package("bookshelf.repositories")
libs = Package("bookshelf.libs")

current = Package("bookshelf.implemented")


class BuySubscription(Injector):

    buy_subscription = usecases.BuySubscription.buy
    load_category = repositories.load_category
    load_price = repositories.load_price
    load_profile = repositories.load_profile
    decrease_balance = repositories.decrease_balance
    current_date = django.utils.timezone.now
    create_subscription = repositories.create_subscription
    send_notifications = current.SendNotifications.send


class PutMoneyIntoAccount(Injector):

    put = usecases.PutMoneyIntoAccount.put
    load_profile = repositories.load_profile
    add_balance = repositories.add_balance
    send_notifications = current.SendNotifications.send


class SignUp(Injector):

    register_user = usecases.SignUp.register_user
    validate_password = libs.validate_password
    create_user = repositories.create_user
    save_password = repositories.save_password
    create_profile = repositories.create_profile
    # FIXME: Don't pass request object to the view.  Inject it is the
    # Store class.
    store_user_in_session = django.contrib.auth.login
    send_notifications = current.SendNotifications.send


class SendNotifications(Injector):

    send = usecases.SendNotifications.send
    create_notifications = repositories.create_notifications
