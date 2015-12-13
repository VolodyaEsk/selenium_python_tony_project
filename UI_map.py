
contact_page_map = dict(first_name_field_xpath="//input[contains(@name, 'first')]",
                        last_name_field_xpath="//input[contains(@name, 'last')]",
                        email_field_xpath="//div/label[contains(text(), 'Email')]/following-sibling::div/input",
                        comment_field_xpath="//textarea",
                        submit_button_xpath="//span[.='Submit']",
                        thank_you_message_xpath="//div[contains(text(), 'Thank you')]"
                        )

product_page_map = dict(quantity_drop_down_id="wsite-com-product-option-Quantity",
                        facebook_share_link_xpath="//a[@title='Share on Facebook']",
                        twitter_share_link_xpath="//a[@class='wsite-com-product-social-twitter']"
                        )

facebook_login_page_map = dict(username_field_id="email",
                               password_filed_id="pass",
                               login_button_name="login"
                               )

facebook_share_page_map = dict(share_link_button_name="share")

twitter_login_page_mao = dict(username_field_id="username_or_email",
                              password_field_id="password",
                              login_button_xpath="//input[@class='button selected submit']"
                              )

twitter_share_page_map = dict(tweet_link_button_xpath="//input[@id='char-count']/following-sibling::input")