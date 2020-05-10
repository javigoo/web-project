Feature: Add playlist
  In order to keep track of the playlists I created,
  As a user
  I want to a add a playlist together with its name and songs

Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Add just playlist name
    Given I login as user "spotiflywebproject@gmail.com" with password "spotifly1234."
    When I add playlist
      | name        |
      | Temazos     |
    Then I'm viewing the details page for playlist by "user"
      | name        |
      | Temazos     |
    And There are 1 playlist