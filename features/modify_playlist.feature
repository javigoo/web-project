Feature: Modify Playlist
  In order to keep updated my previous playlists
  As a user
  I want to edit a playlist register I created

  Background: There are registered users and playlist by one of them
    Given Exists a user "user1" with password "password"
    And Exists restaurant registered by "user1"
      | name           |
      | Gaby's playlist|

  Scenario: Edit owned playlist name
    Given I login as user "user1" with password "password"
    When I view the details for name "Javi's playlist"
    And I edit the current playlist
      | name           |
      | Javi's playlist|
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user2"
      | name            |
      | Javi's playlist |
    And There are 1 playlist
