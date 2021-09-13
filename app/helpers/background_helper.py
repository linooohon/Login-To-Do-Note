import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from app.helpers.updatedashboard_helper import fetch_spotify_youtube
from app.helpers.sendsoulmate_helper import check_same_song_lover
from app.helpers.updateuserplaylist_helper import update_user_playlist


class BackgroundHelper():
    def __init__(self, app):
        self.app = app
        self.trigger_background_job(
            self.dashboard_background_update, 1, '2021-9-13 18:00:00')
        self.trigger_background_job(
            self.soulmate_email_background_sending, 1, '2021-9-12 00:00:00')
        self.trigger_background_job(
            self.user_playlist_background_update, 1, '2021-9-13 13:00:00')
        # self.trigger_background_job(
        #     self.user_playlist_background_update, 30)

    #  Prevent call this function twice in Flask -> https: // stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice/25504196
    def dashboard_background_update(self):
        with self.app.app_context():
            # if is_running_from_reloader():   # Prevent call this function twice
            fetch_spotify_youtube()

    def soulmate_email_background_sending(self):
        with self.app.app_context():
            check_same_song_lover()

    def user_playlist_background_update(self):
        with self.app.app_context():
            update_user_playlist()

    def trigger_background_job(self, event, period, start_date=None):
        scheduler = BackgroundScheduler(
            {'apscheduler.timezone': 'UTC'})
        scheduler.add_job(func=event,
                          trigger="interval", days=period, start_date=start_date)
        scheduler.start()

    # if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    # https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html?highlight=days

    # Shut down the scheduler when exiting the app
    # atexit.register(lambda: scheduler.shutdown())