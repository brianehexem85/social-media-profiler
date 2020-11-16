# -*- coding: utf-8 -*-
"""The main analyzing module."""

from concurrent.futures import ProcessPoolExecutor

from app.backend.analyzing.facebook.facebook import caller_analyze_facebook
from app.backend.analyzing.instagram.instagram import caller_analyze_instagram
from app.backend.analyzing.linkedin.linkedin import caller_analyze_linkedin
from app.backend.analyzing.twitter.twitter import caller_analyze_twitter


def main_analyzing(scraping_response: dict, user_input: dict) -> dict:
    """
    Take scraping response and run filters according to the user input.

    Args:
        scraping_response: the dict that has been received after scraping.
        user_input: user input represented as a dict.
    Returns:
        dict: the dictionary with filtered profiles from all social media.
    """
    with ProcessPoolExecutor(max_workers=4) as pool:
        facebook_process = pool.submit(
            caller_analyze_facebook, scraping_response=scraping_response, user_input=user_input
        )
        instagram_process = pool.submit(
            caller_analyze_instagram, scraping_response=scraping_response, user_input=user_input
        )
        linkedin_process = pool.submit(
            caller_analyze_linkedin, scraping_response=scraping_response
        )
        twitter_process = pool.submit(
            caller_analyze_twitter, scraping_response=scraping_response, user_input=user_input
        )
    analysis_results = {
        **facebook_process.result(),
        **instagram_process.result(),
        **linkedin_process.result(),
        **twitter_process.result(),
        "google_search":  scraping_response["google_search"]
    }
    return analysis_results


if __name__ == "__main__":
    to_analyze = {'facebook': [{'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/WPXIAmyMarcinkiewicz/', 'Profile name: ': 'WPXI Amy Marcinkiewicz'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amy.butler.906/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amy.butler.566/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amy.b.brunson/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amy.butlerr/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amy.l.butler.5/', 'Profile name: ': 'Amy Louise Butler'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amybutlerdesign/'}], 'google_search': {'name': []}, 'instagram': [{'username': 'amylibbybutler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/52717203_466360340568832_6869589027884892160_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=p9Hmjhby6dEAX8Ic6Bq&_nc_tp=25&oh=576530ab538b1e2768cadaf858bdaf49&oe=5FDBA513', 'media_count': 832, 'follower_count': 1210, 'following_count': 486, 'biography': '•Beau’s Momma 👶🏼\n•Fur-babies=#tacothefrenchie and Homer 🐶❤️🐱\n•Farmers Wife 👰🏻💍👨🏻\u200d🌾 @benwbutler', 'whatsapp_number': ''}, {'username': 'amybutlerrrx', 'full_name': '𝐀𝐌𝐘 𝐁𝐔𝐓𝐋𝐄𝐑🤍', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/123144421_644864636193381_2238950747881713350_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=EIPLXEcK0cMAX8TepKG&_nc_tp=25&oh=fdb849eba01f27135da09a6ac800c5fa&oe=5FDB131F', 'media_count': 7, 'follower_count': 1137, 'following_count': 1026, 'biography': 'Oscar xx\n👻amybutlerrr', 'public_email': '', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'amy_spam.48', 'full_name': 'amy butler💋', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/26433715_1094395954036091_8331162322789728256_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=4TkJ43BcQ6IAX_2BbZI&_nc_tp=25&oh=a21adb3fe6acc968cc3ce42d0dc3b214&oe=5FD92587', 'media_count': 34, 'follower_count': 595, 'following_count': 412, 'biography': 'welcome to my spam account🤝💕', 'whatsapp_number': ''}, {'username': 'amybutlerdesign', 'full_name': 'Amy Butler & Blossom Magazine', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/33466837_246972862740531_1361337369625624576_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=X5NIYhTvhioAX8xcvTg&_nc_tp=25&oh=659e3439a461cb9b044d0d305aa36ad0&oe=5FDAF40B', 'media_count': 2743, 'follower_count': 40510, 'following_count': 748, 'biography': 'We celebrate vibrant living & exploring inspirations for spirit, home, nature and handmade. Global retreats. Express love, create beauty, be kind.', 'whatsapp_number': ''}, {'username': 'amybutler_x_x_', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/108305675_289728225472582_6760628535725680429_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=JxZNeyItyjAAX8kxSsF&_nc_tp=25&oh=2a00612500ed50403ef1c147bb043ea0&oe=5FD9B6FB', 'media_count': 76, 'follower_count': 412, 'following_count': 460, 'biography': 'If you want to see lots of dogs, this is the right profile for you 🥰', 'whatsapp_number': ''}, {'username': 'moonshineandminibuses', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/104262422_729343484482057_8071247393614134077_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=0mar8YaGW5MAX9zEDSr&_nc_tp=25&oh=322be4866d0f802f40cb55aecc7488fb&oe=5FDA8646', 'media_count': 9, 'follower_count': 56, 'following_count': 12, 'biography': 'American expat living in Ukraine 🇺🇦\nSlow traveling Eastern Europe and the Caucasus since 2016 👀\nDrinking all the drinks since way before then. 🥤', 'whatsapp_number': ''}, {'username': 'amybutler_hair', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/74607447_630451424152593_7569128239923200_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=kjdK83BaVmoAX8ubin3&_nc_tp=25&oh=9dbd33bb89634cb521a9c360614fd4c2&oe=5FDB32D7', 'media_count': 91, 'follower_count': 347, 'following_count': 299, 'biography': 'Stylist at Design One Salon & Spa ✨💇🏼\u200d♀️ \nDM me or CALL 804-794-4247 to book an appointment\n#hairbyamymae', 'public_email': '', 'public_phone_number': '8047944247', 'whatsapp_number': ''}, {'username': 'fullwifehappylife', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/109045911_606886636918214_3663472381902009985_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=hTXyGUDwVYUAX_Q0l3x&_nc_tp=25&oh=cafa38e63373c3fa7b5c6cf5ac9cb22c&oe=5FDB7549', 'media_count': 25, 'follower_count': 265, 'following_count': 187, 'biography': 'Mom 🤱🏻\nFarmers Wife 🧑🏼\u200d🌾👩🏻\u200d🌾\nWannabe Chef👩🏻\u200d🍳\nThe secret to a happy life is a full wife!', 'public_email': '', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'faunarie.art', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/118980372_176951260621483_2493833730321935133_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=40_3FzR_n3AAX-kxrrb&_nc_tp=25&oh=d57af8cdeeb490c7ad03fe2dc5dafd36&oe=5FDADD50', 'media_count': 134, 'follower_count': 255, 'following_count': 537, 'biography': 'Watercolours, bunnies, also sometimes other things!\nCommissions available on request.\n https://blacklivesmatters.carrd.co/', 'public_email': 'amy@timeistheanswer.com', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'butler.amyb', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/76833511_524068734847865_6027356682852499456_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=xWpCkO_qGWkAX9u_MLA&_nc_tp=25&oh=9773cf456ba06fd976fa1982c4fdde95&oe=5FDABF34', 'media_count': 440, 'follower_count': 458, 'following_count': 741, 'biography': 'Christ Follower💕 Wife,Mom,Goofy Aunt•I help ppl Feel Better, Look Better & Live BIGGER.     AmyButler.arbonne.com', 'whatsapp_number': ''}, {'username': 'amy.butler1', 'full_name': 'amy butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/124979459_755002018698986_1416357715755042023_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=uBYG2uzBAXoAX_3w6Gb&_nc_tp=25&oh=9c7c9e90ee3446704250aea246e552b2&oe=5FDA7695', 'media_count': 1, 'follower_count': 1060, 'following_count': 1577, 'biography': 'amybutler14👻\ncome here often❓', 'public_email': '', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'fabasitgets', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/65772397_2160093554116230_6919818726246187008_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=LDIr5hJ_gksAX_8GvcS&_nc_tp=25&oh=6082093335d29c708510643541dd04a1&oe=5FDC6668', 'media_count': 272, 'follower_count': 181, 'following_count': 441, 'biography': 'Problematic in the relatable sense\nArt account @faunarie.art\nhttps://blacklivesmatters.carrd.co', 'whatsapp_number': ''}, {'username': 'amy_butler_events', 'full_name': 'A-BE', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/95956417_599560840657483_2468102325286207488_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=CN_JquS0HMYAX8ARxN5&_nc_tp=25&oh=3a9e599bc41f60211aac312c114897c6&oe=5FD9D6F6', 'media_count': 54, 'follower_count': 141, 'following_count': 259, 'biography': '✨Celebrant ✨Event planner ✨Event management 💒 Weddings ⛪️ Baby naming 💀 Funerals 🥳 Parties 🎈Corporate 📚Conferences \n👩 \n📞 07894010944\n📧 info@a-be.co.uk', 'public_email': 'info@a-be.co.uk', 'public_phone_number': '7894010944', 'whatsapp_number': ''}, {'username': 'amy.butler.37669', 'full_name': 'FlabbyAbby', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/117326752_812199132648157_467019235893727489_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=mR5NBuxJKx4AX9JmzxG&_nc_tp=25&oh=01df035df03eea708564e5b2c6c3cc12&oe=5FD953CB', 'media_count': 115, 'follower_count': 118, 'following_count': 185, 'biography': "I'm soon to be a single mom, reaching for set goals!", 'whatsapp_number': ''}, {'username': 'amybutler040419', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/70149154_2478517002239302_6321182168735285248_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=v-DSIChlq0YAX93XYkF&_nc_tp=25&oh=aa5c2bad5a3b3cf03a77e00b01d00cc4&oe=5FDCD54F', 'media_count': 59, 'follower_count': 259, 'following_count': 371, 'biography': 'Conscious sleep educator and parenting coach! Offering gentle, respectful and compassionate strategies to resolve your parenting struggles!', 'public_email': 'amy@compassfamilyconsultants.com', 'public_phone_number': '7782359756', 'whatsapp_number': ''}, {'username': 'amybutler60', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/11328229_667448370051818_1009314918_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=mEGUxsKuLVUAX8XPA7A&oh=4616714ad3eb6497987f8c991ba6e5b3&oe=5FDA053C', 'media_count': 206, 'follower_count': 273, 'following_count': 164, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy.davai', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/66124745_2295960340677778_386498201387008000_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=8xbV_jT1XTwAX8uR4LD&_nc_tp=25&oh=feae391db7243aef08d11c03300e9bea&oe=5FD95669', 'media_count': 1028, 'follower_count': 1067, 'following_count': 808, 'biography': "Давай, давай!\n✈️ * 🍸* 🤦\u200d♀️ * ✍️\n🌍 Based in Kyiv, Ukraine! 🇺🇦\nPolish Road Trip? Cocktails on the Trans Siberian? Expat life? It's all there 👇", 'whatsapp_number': ''}, {'username': 'a.butler1', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/924635_739762569471644_1884492400_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=p3qxs1l-R_EAX94q6Qk&oh=bf9b6b8b8f7a8c4017be75dd0a4baf6b&oe=5FDC8E91', 'media_count': 223, 'follower_count': 127, 'following_count': 511, 'biography': '', 'whatsapp_number': ''}, {'username': 'sfsuperstar', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/70000857_2546939038693245_3453321055089721344_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=rVMp8K8kD8QAX-fSJyY&_nc_tp=25&oh=3b41b2e8412e913814df14331d5dab5e&oe=5FD9DF26', 'media_count': 766, 'follower_count': 357, 'following_count': 1092, 'biography': 'seeker at heart 💜\ninfused with magic 🔮\nSupport Planting Justice! \nhttps://www.gofundme.com/the-good-table-cafe-and-planting-justice-nursery', 'whatsapp_number': ''}, {'username': 'amy.butler416', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/123469435_215181863355532_4851193719831013292_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=5B1n3OHkGaUAX98gH5K&_nc_tp=25&oh=66a9c51c79fe821393348245038ea966&oe=5FD97FEF', 'media_count': 103, 'follower_count': 523, 'following_count': 1110, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy_31284', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/17266071_1689575861342684_8716365316659085312_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=ZaMQonRjR9QAX_KdCD8&_nc_tp=25&oh=3d0a63063f117530d27f9c884c0abf31&oe=5FD91DAE', 'media_count': 381, 'follower_count': 735, 'following_count': 4624, 'biography': 'Just me. Mom of a Type 1 Diabetic', 'whatsapp_number': ''}, {'username': 'amybutler12343', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/103492554_264640084643104_25939593562978261_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=Grf00FFnf1QAX93l1Ds&_nc_tp=25&oh=7e303e6b942d75000f334423bb715ff3&oe=5FDC7370', 'media_count': 3, 'follower_count': 80, 'following_count': 97, 'biography': 'Add my snap amybutler123434 xx', 'public_email': '', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'amybutler1984', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/17932474_293641287725475_64055430015352832_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=q9WKKU6HtV4AX_5I-I0&_nc_tp=25&oh=f66999311fe74abcaff731b9318e0883&oe=5FDA8722', 'media_count': 6, 'follower_count': 127, 'following_count': 50, 'biography': 'Train manager for LNER. West ham and NASCAR fan. Goalkeeper for Cambridge Utd WFC', 'whatsapp_number': ''}, {'username': 'amybutler___', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/123130640_348114549825787_9089570466600923982_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=JTZfMkOd4GsAX_2EZRc&_nc_tp=25&oh=7fa1d786d86dcc28b9c28de0c5b74edd&oe=5FD9DE28', 'media_count': 7, 'follower_count': 1363, 'following_count': 1791, 'biography': '@georgesfc04 💕', 'public_email': 'amybutler626@gmail.com', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'amybutler0102', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/124327275_374913303822456_7369191457314039486_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=a0EGpqh1c9EAX8CrZ55&_nc_tp=25&oh=cbd68141e500c7dbfd7f25df640945fc&oe=5FD90EE1', 'media_count': 35, 'follower_count': 1372, 'following_count': 1700, 'biography': 'snapchattt~~amybutler0102 ❤', 'public_email': 'amybutler20002@gmail.com', 'public_phone_number': '892009779', 'whatsapp_number': ''}, {'username': 'amy4805', 'full_name': 'amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/59595279_2298275316899069_3830265355129847808_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=qdz3NfJNFxYAX_dlHW4&_nc_tp=25&oh=70125b52070599cb40732bd4725456ba&oe=5FDCC195', 'media_count': 598, 'follower_count': 468, 'following_count': 1399, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy.butler2665', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/72525163_2586183951494887_8500794942363271168_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=bCLBkYUWGBMAX_LALVc&_nc_tp=25&oh=26f40fa939e6f36c9344ec00130611c2&oe=5FDC6E86', 'media_count': 162, 'follower_count': 67, 'following_count': 302, 'biography': '💁🏻\u200d♀️Wife, Mom, Daughter, Sister, Aunt\n🏁Crew Chief @butlerracing\n💼Account Admin @PSEHousing / @legacyglobalsports\n💄Indep Sales Rep @avoninsider', 'whatsapp_number': ''}, {'username': 'apb92', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/37126887_522103204876734_8451301663389515776_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=iDGaIzMI_GQAX8VT9ts&_nc_tp=25&oh=2381d18508630a89c7df66dd6678ad11&oe=5FD995C2', 'media_count': 31, 'follower_count': 375, 'following_count': 405, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy_lynne_designs', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/44000082_758125774534908_2736210427468840960_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=SRDE-ezqNeIAX-xSSA6&_nc_tp=25&oh=3099954310dfcd2fa30ae9fd1a909bc9&oe=5FDA1E6C', 'media_count': 242, 'follower_count': 1253, 'following_count': 181, 'biography': 'Maker of lovely purses, wristlets, totes, pillows, and patterns! #amylynnedesigns  #bagdesigner #patternsbyamylynne #thebutlermethod #youtuber', 'public_email': 'alb@amylynnedesign.biz', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'amybutler661', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/97558822_958663911274860_1824783844310515712_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=vkSnfZTMq0QAX9bcYfZ&_nc_tp=25&oh=9d0df8662065d449de2af1b692116565&oe=5FD9F743', 'media_count': 75, 'follower_count': 44, 'following_count': 75, 'biography': '', 'whatsapp_number': ''}, {'username': 'amieebutler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/94471046_1700706200071760_4195274353371250688_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=59b372PfeAAAX9iRryL&_nc_tp=25&oh=ae2b5043d79a3a4beb73b9b6cd52b42d&oe=5FDBBD41', 'media_count': 207, 'follower_count': 328, 'following_count': 612, 'biography': 'Snapchat Amerz34', 'whatsapp_number': ''}, {'username': 'amyyybutler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/70598432_663923094117433_7841058107085029376_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=RnWgaFDcOiwAX_ao6CQ&_nc_tp=25&oh=abdaee1cf62f1e9e7d1c6f468da0d969&oe=5FDB18AD', 'media_count': 270, 'follower_count': 446, 'following_count': 538, 'biography': '', 'whatsapp_number': ''}, {'username': 'amyy.butler', 'full_name': 'amy butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/124974242_1791220327705124_6591973958510276340_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=XT-9iLsakVIAX865xdy&_nc_tp=25&oh=2c27d82937aad051d787452917525764&oe=5FDA6762', 'media_count': 5, 'follower_count': 188, 'following_count': 235, 'biography': 'she/her | 15\n🦋🌞🐉💞', 'whatsapp_number': ''}, {'username': 'amity_calamity', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/49907409_2350415558528871_1995897703615168512_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=QTVkvQpt17MAX_2Wofx&_nc_tp=25&oh=18aec3d261a58adae3e4eb7308dfb90a&oe=5FDBFD03', 'media_count': 476, 'follower_count': 534, 'following_count': 1255, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy_butler_creations', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69857929_369086100662385_4568532351700697088_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=a9gVXq133qwAX-A4RWn&_nc_tp=25&oh=e29cd2dbdbcdb1ee1e141c03408811bb&oe=5FDC4CD7', 'media_count': 26, 'follower_count': 47, 'following_count': 30, 'biography': 'Alterations and tailoring. Also so make a few bespoke items; skirts, dresses, bunting and blankets.', 'public_email': 'amybutlercreations@gmail.com', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'amy_butler_xoxo', 'full_name': 'Amy_butler_xoxo', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/11358957_836590156423645_766697210_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=VC5Cq8kVcvcAX89UqJ8&oh=eec25306ea4ec3e0c38dac970c32cd9a&oe=5FD9FCF8', 'media_count': 7, 'follower_count': 63, 'following_count': 159, 'biography': 'Love my bæ he is so funny 💖💚💋😘', 'whatsapp_number': ''}, {'username': 'amy._.butler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/11190168_853333071418465_133683509_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=XdFiQXZNQloAX_GuL5y&oh=a24c067723c4430e0fa7f2864772b2e3&oe=5FDC60CE', 'media_count': 4, 'follower_count': 0, 'following_count': 19, 'biography': '💩No one to love No problem💩', 'whatsapp_number': ''}, {'username': 'amy_butlerrrr', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/101550815_283765722809165_2350103377343414272_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=Rs5ZLUxLQ5AAX89NUzG&_nc_tp=25&oh=4df63eb046ff695e63549a77993093f0&oe=5FDB163D', 'media_count': 32, 'follower_count': 95, 'following_count': 709, 'biography': 'Living life the best I can. ❤️', 'whatsapp_number': ''}, {'username': 'amy_butler_97', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/119467508_773579539851439_1013334478779119509_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=883Bwh_SUf4AX_5MP3Z&_nc_tp=25&oh=0e3ff296b950a5f133f8109c1d43dacb&oe=5FDC03F2', 'media_count': 1, 'follower_count': 32, 'following_count': 17, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy.butler.3781995', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/21107864_500455946998325_9113169433806766080_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=02T6uBFBJ4sAX8kmEya&_nc_tp=25&oh=ff0d19e5080e9c0c554c770a44249ca5&oe=5FDB8889', 'media_count': 5, 'follower_count': 132, 'following_count': 168, 'biography': '', 'whatsapp_number': ''}, {'username': 'amybutler0155', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/104419713_2702987776650893_8985120017958999970_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=-CaL1_pinNQAX_tW7pC&_nc_tp=25&oh=dc6949ef68bb9f2fea090372659a6607&oe=5FDA364E', 'media_count': 8, 'follower_count': 81, 'following_count': 125, 'biography': '', 'whatsapp_number': ''}, {'username': 'blushandblossomboutiquespa', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/106694297_621009155515486_7990670946846173307_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=Vw15g0pd620AX-brn6e&_nc_tp=25&oh=0769ba29d6b17cd566e24ca2b57d79a5&oe=5FDBF817', 'media_count': 527, 'follower_count': 2680, 'following_count': 1129, 'biography': 'Blush + Blossom Boutique + Spa. \n 📦Delivery + pick up + online sales + gift boxes\n👩🏻\u200d🎨ETHICAL MUA\n💄 Organic beauty bar+boutique\n🌱Conscious Beauty', 'public_email': 'blushandblossomspa@outlook.com', 'public_phone_number': '2505151805', 'whatsapp_number': ''}, {'username': 'mrs.amy_butler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/72070532_2446540882338494_1583377747080642560_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=q4Oj0X-x_tEAX8KaNtg&_nc_tp=25&oh=0634693460e5b24fd64ce52c588a95ca&oe=5FD9A846', 'media_count': 7, 'follower_count': 84, 'following_count': 220, 'biography': '', 'whatsapp_number': ''}, {'username': 'pastoramynyc', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/66472254_1301998926645322_3266026902929801216_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=Oxg_A8sm9ckAX9xErTn&_nc_tp=25&oh=e21a3f285fea375b67aa386f4349e9d1&oe=5FD8FA69', 'media_count': 184, 'follower_count': 1620, 'following_count': 95, 'biography': '', 'whatsapp_number': ''}, {'username': 'amy.butler.54', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/118669214_1313609628975739_6186021794611040071_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=w2uIoXmjf7YAX9hd7ng&_nc_tp=25&oh=30e3f2453018c7231ecaf598cc41f8e7&oe=5FD90B3F', 'media_count': 0, 'follower_count': 179, 'following_count': 203, 'biography': '', 'whatsapp_number': ''}, {'username': 'amybutler_', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/118285434_642199363347367_8982478062752860180_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=tL3CJW9VtjQAX9hJxeg&_nc_tp=25&oh=4a62204cf3f18b4cd3bf2874991ef253&oe=5FD8F181', 'media_count': 223, 'follower_count': 199, 'following_count': 811, 'biography': '🌸', 'whatsapp_number': ''}, {'username': 'amy__butler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/66640727_475734116544265_8846577502324260864_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=IHvxIg0vSs0AX_vjOhK&_nc_tp=25&oh=fa068330302420a9b17bb67865966596&oe=5FDB4191', 'media_count': 7, 'follower_count': 437, 'following_count': 464, 'biography': 'New Zealand • Harvard ‘23', 'whatsapp_number': ''}, {'username': '_amyloo', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/120601189_176971013923237_3560198693907704209_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=XRn_PGF9CYEAX_BIis6&_nc_tp=25&oh=528bff7eab3e1c7d9f1da7aea82d79a5&oe=5FD91CBB', 'media_count': 190, 'follower_count': 589, 'following_count': 1665, 'biography': 'Mai-Ella Rose👧 14/08/16 💜💝\nJaxon Lee 🧒 26/11/18 💚💙', 'whatsapp_number': ''}, {'username': 'amybutler180', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/10597492_329576970540353_91862948_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=mfZVNVVnwzwAX8OBG0d&oh=f55e655545f35174805e17711090cacc&oe=5FDA8828', 'media_count': 499, 'follower_count': 168, 'following_count': 487, 'biography': '', 'whatsapp_number': ''}, {'username': 'olwyngdh', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/11909326_1039325552758406_2099283165_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=VYbXeBXigQEAX-L8cDA&oh=8ad3f879aee409498d699a3419f34729&oe=5FDB1534', 'media_count': 358, 'follower_count': 321, 'following_count': 626, 'biography': '', 'whatsapp_number': ''}, {'username': 'btherein5mins', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/101013019_537621216922266_3963678936403017728_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=RWEaoa19Se8AX9qx_nY&_nc_tp=25&oh=fba5dfd5c518f6edaadf4f76bfd22f0a&oe=5FDA2334', 'media_count': 58, 'follower_count': 35, 'following_count': 646, 'biography': 'YL + Essential Oils • do what makes u happy 😊 treat yourself like someone u love 💕 don’t worry about things u cannot control • try & choose J🤍Y', 'whatsapp_number': ''}, {'username': 'ms_amy_butler', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/17817548_1853697278224347_2919856932623745024_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=2xSTIc4x13sAX8aQc89&_nc_tp=25&oh=ec350792b449618624bd5591d2ef64b6&oe=5FD9184A', 'media_count': 1143, 'follower_count': 359, 'following_count': 485, 'biography': 'Mom to 2 amazing girls. 💯 Strong, Fitness Loving, plant based, cruelty free, Online Personal Trainer and Wellness Coach', 'whatsapp_number': ''}, {'username': 'amy_main.48', 'full_name': 'amy butler💋', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/26153269_1533043733397345_909101519792504832_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=P0F6qWOK48MAX-bu3Zn&_nc_tp=25&oh=884cfad9c347732e6db39a59c5f69a8e&oe=5FDA1331', 'media_count': 19, 'follower_count': 283, 'following_count': 292, 'biography': '13💕single💕👻 - amy_louise20xx', 'whatsapp_number': ''}, {'username': 'amy_butler_xoxox', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/11377495_605264112909870_1084447874_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=kdeoJA8uxZoAX8-Uhlh&oh=df7575ac2b6b2204a86751e715d2ecb3&oe=5FDA48CC', 'media_count': 0, 'follower_count': 2, 'following_count': 1, 'biography': '', 'whatsapp_number': ''}, {'username': 'amyb4598', 'full_name': 'Amy Butler', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/118699930_2893031247595444_1975072983510346547_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=wL4Mkr-hM4YAX-Ntohe&_nc_tp=25&oh=39bca555ed0ed22cc48672dd33eb5750&oe=5FDC1E6B', 'media_count': 2, 'follower_count': 57, 'following_count': 154, 'biography': 'Dream big, stay focused & make it happen 🥰', 'whatsapp_number': ''}], 'linkedin': {'potential_subjects_after_filtering': [{'industryName': 'Professional Training', 'lastName': 'Butler', 'locationName': 'Ukraine', 'student': False, 'geoCountryName': 'Ukraine', 'firstName': 'Amy', 'headline': 'Director Of Studies at The London School of English', 'experience': [{'locationName': 'Kyiv, Kyiv City, Ukraine', 'entityUrn': 'urn:li:fs_position:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,1661935551)', 'geoLocationName': 'Kyiv, Kyiv City, Ukraine', 'geoUrn': 'urn:li:fs_geo:104035893', 'companyName': 'The London School of English', 'timePeriod': {'startDate': {'month': 8, 'year': 2020}}, 'company': {'employeeCountRange': {'start': 11, 'end': 50}, 'industries': ['Education Management']}, 'title': 'Director Of Studies', 'region': 'urn:li:fs_region:(ua,0)', 'companyUrn': 'urn:li:fs_miniCompany:17965036', 'companyLogoUrl': 'https://media-exp1.licdn.com/dms/image/C4E0BAQGIfzBvOBNviA/company-logo_'}, {'$anti_abuse_annotations': [{'attributeId': 26, 'entityId': 2}, {'attributeId': 14, 'entityId': 2}, {'attributeId': 16, 'entityId': 2}, {'attributeId': 36, 'entityId': 2}], 'entityUrn': 'urn:li:fs_position:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,718472906)', 'companyName': 'Freelance', 'timePeriod': {'startDate': {'month': 1, 'year': 2015}}, 'description': '•\tTravel writing for a New York City blog with a focus on international tourists, SuperTravelersUSA.\n•\tCopy writing for event ticketing website.\n•\tSkills-focused ESL activities for adult education curriculum. \n\nSamples available upon request.', 'title': 'Writer'}, {'locationName': 'Kiev Region, Ukraine', 'entityUrn': 'urn:li:fs_position:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,1504137723)', 'geoLocationName': 'Kiev Region, Ukraine', 'geoUrn': 'urn:li:fs_geo:100220281', 'companyName': 'The London School of English', 'timePeriod': {'endDate': {'month': 8, 'year': 2020}, 'startDate': {'month': 8, 'year': 2019}}, 'description': '• Planned and conducted communicative lessons for primary levels through to adult Cambridge preparation classes.\n• Mentored teachers through observations and feedback. \n• Conducted in-house teacher training to familiarize teachers with school procedures. \n• Re-wrote existing progress and end-of-course tests to comply with new internal standards.\n• Re-wrote course pacing guides for online teaching during quarantine and managed school-wide materials development. \n• Created course book-based materials to be used by teachers company-wide for online teaching.\n• Conducted teacher training webinars through Dinternal Education, the exclusive Pearson distributor in Ukraine.', 'company': {'employeeCountRange': {'start': 11, 'end': 50}, 'industries': ['Education Management']}, 'title': 'Senior Teacher', 'region': 'urn:li:fs_region:(ua,10183)', 'companyUrn': 'urn:li:fs_miniCompany:17965036', 'companyLogoUrl': 'https://media-exp1.licdn.com/dms/image/C4E0BAQGIfzBvOBNviA/company-logo_'}, {'locationName': 'Moscow, Russian Federation', '$anti_abuse_annotations': [{'attributeId': 26, 'entityId': 2}, {'attributeId': 14, 'entityId': 2}, {'attributeId': 16, 'entityId': 2}, {'attributeId': 36, 'entityId': 2}], 'entityUrn': 'urn:li:fs_position:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,1402656676)', 'geoLocationName': 'Moscow, Russian Federation', 'companyName': 'English Playschool Moscow', 'timePeriod': {'endDate': {'month': 7, 'year': 2019}, 'startDate': {'month': 9, 'year': 2018}}, 'description': '• Improved ‘zero beginner’ very young learners’ language skills using a variety of techniques, including mini-lessons, immersion strategies, and assessments based on IB principles. \n• Utilized CLIL approaches to teach academic subjects to various age groups and proficiency levels.\n• Collaborated with a team of local Russian assistants. \n\n', 'title': 'English Teacher for Very Young Learners'}, {'locationName': 'Tbilisi, Georgia', '$anti_abuse_annotations': [{'attributeId': 26, 'entityId': 2}, {'attributeId': 14, 'entityId': 2}, {'attributeId': 16, 'entityId': 2}, {'attributeId': 36, 'entityId': 2}], 'entityUrn': 'urn:li:fs_position:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,1212137253)', 'geoLocationName': 'Tbilisi, Georgia', 'companyName': 'American Councils', 'timePeriod': {'endDate': {'month': 5, 'year': 2018}, 'startDate': {'month': 1, 'year': 2018}}, 'description': '• Created customized English for Special Purposes tracks for individual students, focusing on topics such as Medical and Academic English. \n• Trained students one-to-one in preparation for the TOEFL exam.\n\n', 'title': 'English Teacher'}], 'skills': [{'name': 'Social Media'}, {'name': 'Editing'}, {'name': 'Microsoft Office'}, {'name': 'Microsoft Excel'}, {'name': 'PowerPoint'}, {'name': 'Social Networking'}, {'name': 'Microsoft Word'}, {'name': 'Copy Editing'}, {'name': 'Outlook'}, {'name': 'Creative Writing'}, {'name': 'CELTA'}, {'name': 'Marketing Communications'}, {'name': 'Research'}, {'name': 'Marketing'}, {'name': 'Teaching'}, {'name': 'Social Media Marketing'}, {'name': 'Blogging'}, {'name': 'Public Speaking'}, {'name': 'Writing'}], 'education': [{'entityUrn': 'urn:li:fs_education:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,569699827)', 'school': {'objectUrn': 'urn:li:school:12691', 'entityUrn': 'urn:li:fs_miniSchool:12691', 'active': True, 'schoolName': 'University of Cambridge', 'trackingId': 'JUd8FrIySNSBu9oPk2ZEPA==', 'logoUrl': 'https://media-exp1.licdn.com/dms/image/C510BAQH4Fc203kgKag/company-logo_'}, 'grade': 'Pass', 'timePeriod': {'startDate': {'year': 2018}}, 'degreeName': 'Delta Module 2', 'schoolName': 'University of Cambridge', 'schoolUrn': 'urn:li:fs_miniSchool:12691'}, {'entityUrn': 'urn:li:fs_education:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,154219575)', 'school': {'objectUrn': 'urn:li:school:12691', 'entityUrn': 'urn:li:fs_miniSchool:12691', 'active': True, 'schoolName': 'University of Cambridge', 'trackingId': 'UScolrfSRaKj/TiFanOkcA==', 'logoUrl': 'https://media-exp1.licdn.com/dms/image/C510BAQH4Fc203kgKag/company-logo_'}, 'grade': 'Pass A', 'timePeriod': {'startDate': {'year': 2013}}, 'degreeName': 'Cambridge CELTA', 'schoolName': 'University of Cambridge', 'schoolUrn': 'urn:li:fs_miniSchool:12691'}, {'entityUrn': 'urn:li:fs_education:(ACoAAAPuxLcBLiAEWc_WChmE4u-yRjL5_HvAYK0,58794249)', 'school': {'objectUrn': 'urn:li:school:18633', 'entityUrn': 'urn:li:fs_miniSchool:18633', 'active': True, 'schoolName': 'University of Michigan', 'trackingId': 'ZvuueFFhS9C1/NO364d0BQ==', 'logoUrl': 'https://media-exp1.licdn.com/dms/image/C4E0BAQFGfERBPGurCg/company-logo_'}, 'timePeriod': {'endDate': {'year': 2009}, 'startDate': {'year': 2007}}, 'degreeName': 'B.A.', 'schoolName': 'University of Michigan', 'fieldOfStudy': 'Film, Screenwriting', 'schoolUrn': 'urn:li:fs_miniSchool:18633'}], 'languages': [], 'publications': [], 'certifications': [], 'honors': []}]}, 'twitter': [({'name': 'Amy Butler', 'screen_name': 'WayfarersBook', 'location': 'Kyiv, Ukraine', 'description': 'Long-term expat, CELTA/Delta qualified English teacher, freelance writer. Insta: wayfarersbook', 'url': 'https://t.co/7fIVtM8Ne0', 'followers_count': 697, 'friends_count': 680, 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1018140475222523904/ADqhB2yj_normal.jpg'}, ['@CailinONeil @VickyFlipFlop @instagram Mine is basically cake, donuts, pasta, and the odd glamour fashion photo. ', "@RoamingRequired Lucky. We've got all sorts of rules because everyone's really paranoid about voter fraud.", "@quickdarshan Embarrassingly, I've never tried before. (Me of little faith in my one vote.) My bf managed to vote i… ", '@RoamingRequired Can you vote by mail? We need to get there. Or online, like Estonia, country of the freaking future.', "@quickdarshan I know it's rigged, it still makes me really mad. Also seeing the clips of governors not being concer… ", 'These lines to vote are insane. We need to start rethinking our voting procedures now. ', "@thethoughtcard I live in Kyiv -- it's a crazy affordable European destination. I've traveled a lot around Ukraine… ", 'RT @inclpablo: me after guessing the password of my own email ', "Man, it's really a shame the cops can't do anything about all those looters. Definitely seems like they're trying.… ", "How do you just walk by an old man bleeding on the ground?!\nDon't turn on the sound unless you want to be ill. ", 'RT @JordanUhl: Who does this protect? ', 'RT @joshfoxfilm: People stuck in traffic are witnessing NYPD beat up folks on their way home. ', "I don't know whether or not this was actually before curfew, but why would you escalate with this tiny group of pea… ", '@gaelemorag Thanks for reading. While the title is provocative, the content itself is more geared towards getting p… ', 'Looking for links to legit places to donate to looted/vandalized #NYC businesses. This article is a good starting p… ', "@RoamingRequired @sunriseon7 Yes, it's embarrassing how we're treating international press. We even got publicly called out by Russia...", 'Your daily reminder that police are abusing and arresting cooperative reporters and journalists. Maybe if they did… ', '@travchats A lot of people are hating on listicles, but if it comes from someone who has done the research, they ca… ', 'This is a super resource for people who are looking to get informed but are also a bit overwhelmed with information… ', 'In case anyone is wondering who is inciting violence, this FBI thread has devastating examples of #PoliceBrutality. '])]}
    taken_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "Cambridge University",
        "twitter_profile": "WayfarersBook",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta qualified teacher",
    }
    print(main_analyzing(to_analyze, taken_input))
