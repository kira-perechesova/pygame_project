import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ееее')
    size = width, height = 1066, 600
    screen = pygame.display.set_mode(size)

    background1_png = pygame.image.load('images/for_levels/background/background1.png').convert_alpha()
    background2_png = pygame.image.load('images/for_levels/background/background2.png').convert_alpha()
    background3_png = pygame.image.load('images/for_levels/background/background3.png').convert_alpha()
    background4_png = pygame.image.load('images/for_levels/background/background4.png').convert_alpha()

    coin_png = pygame.image.load('images/for_levels/coin.png').convert_alpha()
    platform_png = pygame.image.load('images/for_levels/platform.png').convert_alpha()

    animations = {'attack': 0, 'death': 1, 'fallattack': 2, 'hurt': 3, 'idle': 4, 'jump': 5,
                  'jumpattack': 6, 'run': 7, 'runattack': 8, 'squat': 9, 'walk': 10, 'walkattack': 11}

    character1_attack1_png = pygame.image.load('images/character/character1/attack/Attack_1.png').convert_alpha()
    character1_attack2_png = pygame.image.load('images/character/character1/attack/Attack_2.png').convert_alpha()
    character1_attack3_png = pygame.image.load('images/character/character1/attack/Attack_3.png').convert_alpha()
    character1_attack4_png = pygame.image.load('images/character/character1/attack/Attack_4.png').convert_alpha()
    character1_attack5_png = pygame.image.load('images/character/character1/attack/Attack_5.png').convert_alpha()
    character1_attack6_png = pygame.image.load('images/character/character1/attack/Attack_6.png').convert_alpha()

    character1_death1_png = pygame.image.load('images/character/character1/death/Death_1.png').convert_alpha()
    character1_death2_png = pygame.image.load('images/character/character1/death/Death_2.png').convert_alpha()
    character1_death3_png = pygame.image.load('images/character/character1/death/Death_3.png').convert_alpha()
    character1_death4_png = pygame.image.load('images/character/character1/death/Death_4.png').convert_alpha()
    character1_death5_png = pygame.image.load('images/character/character1/death/Death_5.png').convert_alpha()
    character1_death6_png = pygame.image.load('images/character/character1/death/Death_6.png').convert_alpha()
    character1_death7_png = pygame.image.load('images/character/character1/death/Death_7.png').convert_alpha()
    character1_death8_png = pygame.image.load('images/character/character1/death/Death_8.png').convert_alpha()

    character1_fallattack1_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_1.png').convert_alpha()
    character1_fallattack2_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_2.png').convert_alpha()
    character1_fallattack3_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_3.png').convert_alpha()
    character1_fallattack4_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_4.png').convert_alpha()
    character1_fallattack5_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_5.png').convert_alpha()
    character1_fallattack6_png = pygame.image.load(
        'images/character/character1/fallattack/FallAttack_6.png').convert_alpha()

    character1_hurt1_png = pygame.image.load('images/character/character1/hurt/Hurt_1.png').convert_alpha()
    character1_hurt2_png = pygame.image.load('images/character/character1/hurt/Hurt_2.png').convert_alpha()
    character1_hurt3_png = pygame.image.load('images/character/character1/hurt/Hurt_3.png').convert_alpha()
    character1_hurt4_png = pygame.image.load('images/character/character1/hurt/Hurt_4.png').convert_alpha()

    character1_idle1_png = pygame.image.load('images/character/character1/idle/Idle_1.png').convert_alpha()
    character1_idle2_png = pygame.image.load('images/character/character1/idle/Idle_2.png').convert_alpha()
    character1_idle3_png = pygame.image.load('images/character/character1/idle/Idle_3.png').convert_alpha()
    character1_idle4_png = pygame.image.load('images/character/character1/idle/Idle_4.png').convert_alpha()

    character1_jump1_png = pygame.image.load('images/character/character1/jump/Jump_1.png').convert_alpha()
    character1_jump2_png = pygame.image.load('images/character/character1/jump/Jump_2.png').convert_alpha()
    character1_jump3_png = pygame.image.load('images/character/character1/jump/Jump_3.png').convert_alpha()
    character1_jump4_png = pygame.image.load('images/character/character1/jump/Jump_4.png').convert_alpha()
    character1_jump5_png = pygame.image.load('images/character/character1/jump/Jump_5.png').convert_alpha()
    character1_jump6_png = pygame.image.load('images/character/character1/jump/Jump_6.png').convert_alpha()
    character1_jump7_png = pygame.image.load('images/character/character1/jump/Jump_7.png').convert_alpha()
    character1_jump8_png = pygame.image.load('images/character/character1/jump/Jump_8.png').convert_alpha()

    character1_jumpattack1_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_1.png').convert_alpha()
    character1_jumpattack2_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_2.png').convert_alpha()
    character1_jumpattack3_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_3.png').convert_alpha()
    character1_jumpattack4_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_4.png').convert_alpha()
    character1_jumpattack5_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_5.png').convert_alpha()
    character1_jumpattack6_png = pygame.image.load(
        'images/character/character1/jumpattack/JumpAttack_6.png').convert_alpha()

    character1_run1_png = pygame.image.load('images/character/character1/run/Run_1.png').convert_alpha()
    character1_run2_png = pygame.image.load('images/character/character1/run/Run_2.png').convert_alpha()
    character1_run3_png = pygame.image.load('images/character/character1/run/Run_3.png').convert_alpha()
    character1_run4_png = pygame.image.load('images/character/character1/run/Run_4.png').convert_alpha()
    character1_run5_png = pygame.image.load('images/character/character1/run/Run_5.png').convert_alpha()
    character1_run6_png = pygame.image.load('images/character/character1/run/Run_6.png').convert_alpha()

    character1_runattack1_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_1.png').convert_alpha()
    character1_runattack2_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_2.png').convert_alpha()
    character1_runattack3_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_3.png').convert_alpha()
    character1_runattack4_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_4.png').convert_alpha()
    character1_runattack5_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_5.png').convert_alpha()
    character1_runattack6_png = pygame.image.load(
        'images/character/character1/runattack/RunAttack_6.png').convert_alpha()

    character1_squat1_png = pygame.image.load('images/character/character1/squat/Squat_1.png').convert_alpha()
    character1_squat2_png = pygame.image.load('images/character/character1/squat/Squat_2.png').convert_alpha()
    character1_squat3_png = pygame.image.load('images/character/character1/squat/Squat_3.png').convert_alpha()
    character1_squat4_png = pygame.image.load('images/character/character1/squat/Squat_4.png').convert_alpha()

    character1_walk1_png = pygame.image.load('images/character/character1/walk/Walk_1.png').convert_alpha()
    character1_walk2_png = pygame.image.load('images/character/character1/walk/Walk_2.png').convert_alpha()
    character1_walk3_png = pygame.image.load('images/character/character1/walk/Walk_3.png').convert_alpha()
    character1_walk4_png = pygame.image.load('images/character/character1/walk/Walk_4.png').convert_alpha()
    character1_walk5_png = pygame.image.load('images/character/character1/walk/Walk_5.png').convert_alpha()
    character1_walk6_png = pygame.image.load('images/character/character1/walk/Walk_6.png').convert_alpha()

    character1_walkattack1_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_1.png').convert_alpha()
    character1_walkattack2_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_2.png').convert_alpha()
    character1_walkattack3_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_3.png').convert_alpha()
    character1_walkattack4_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_4.png').convert_alpha()
    character1_walkattack5_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_5.png').convert_alpha()
    character1_walkattack6_png = pygame.image.load(
        'images/character/character1/walkattack/WalkAttack_6.png').convert_alpha()

    character2_attack1_png = pygame.image.load('images/character/character2/attack/Attack_1.png').convert_alpha()
    character2_attack2_png = pygame.image.load('images/character/character2/attack/Attack_2.png').convert_alpha()
    character2_attack3_png = pygame.image.load('images/character/character2/attack/Attack_3.png').convert_alpha()
    character2_attack4_png = pygame.image.load('images/character/character2/attack/Attack_4.png').convert_alpha()
    character2_attack5_png = pygame.image.load('images/character/character2/attack/Attack_5.png').convert_alpha()
    character2_attack6_png = pygame.image.load('images/character/character2/attack/Attack_6.png').convert_alpha()

    character2_death1_png = pygame.image.load('images/character/character2/death/Death_1.png').convert_alpha()
    character2_death2_png = pygame.image.load('images/character/character2/death/Death_2.png').convert_alpha()
    character2_death3_png = pygame.image.load('images/character/character2/death/Death_3.png').convert_alpha()
    character2_death4_png = pygame.image.load('images/character/character2/death/Death_4.png').convert_alpha()
    character2_death5_png = pygame.image.load('images/character/character2/death/Death_5.png').convert_alpha()
    character2_death6_png = pygame.image.load('images/character/character2/death/Death_6.png').convert_alpha()
    character2_death7_png = pygame.image.load('images/character/character2/death/Death_7.png').convert_alpha()
    character2_death8_png = pygame.image.load('images/character/character2/death/Death_8.png').convert_alpha()

    character2_fallattack1_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_1.png').convert_alpha()
    character2_fallattack2_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_2.png').convert_alpha()
    character2_fallattack3_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_3.png').convert_alpha()
    character2_fallattack4_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_4.png').convert_alpha()
    character2_fallattack5_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_5.png').convert_alpha()
    character2_fallattack6_png = pygame.image.load(
        'images/character/character2/fallattack/FallAttack_6.png').convert_alpha()

    character2_hurt1_png = pygame.image.load('images/character/character2/hurt/Hurt_1.png').convert_alpha()
    character2_hurt2_png = pygame.image.load('images/character/character2/hurt/Hurt_2.png').convert_alpha()
    character2_hurt3_png = pygame.image.load('images/character/character2/hurt/Hurt_3.png').convert_alpha()
    character2_hurt4_png = pygame.image.load('images/character/character2/hurt/Hurt_4.png').convert_alpha()

    character2_idle1_png = pygame.image.load('images/character/character2/idle/Idle_1.png').convert_alpha()
    character2_idle2_png = pygame.image.load('images/character/character2/idle/Idle_2.png').convert_alpha()
    character2_idle3_png = pygame.image.load('images/character/character2/idle/Idle_3.png').convert_alpha()
    character2_idle4_png = pygame.image.load('images/character/character2/idle/Idle_4.png').convert_alpha()

    character2_jump1_png = pygame.image.load('images/character/character2/jump/Jump_1.png').convert_alpha()
    character2_jump2_png = pygame.image.load('images/character/character2/jump/Jump_2.png').convert_alpha()
    character2_jump3_png = pygame.image.load('images/character/character2/jump/Jump_3.png').convert_alpha()
    character2_jump4_png = pygame.image.load('images/character/character2/jump/Jump_4.png').convert_alpha()
    character2_jump5_png = pygame.image.load('images/character/character2/jump/Jump_5.png').convert_alpha()
    character2_jump6_png = pygame.image.load('images/character/character2/jump/Jump_6.png').convert_alpha()
    character2_jump7_png = pygame.image.load('images/character/character2/jump/Jump_7.png').convert_alpha()
    character2_jump8_png = pygame.image.load('images/character/character2/jump/Jump_8.png').convert_alpha()

    character2_jumpattack1_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_1.png').convert_alpha()
    character2_jumpattack2_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_2.png').convert_alpha()
    character2_jumpattack3_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_3.png').convert_alpha()
    character2_jumpattack4_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_4.png').convert_alpha()
    character2_jumpattack5_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_5.png').convert_alpha()
    character2_jumpattack6_png = pygame.image.load(
        'images/character/character2/jumpattack/JumpAttack_6.png').convert_alpha()

    character2_run1_png = pygame.image.load('images/character/character2/run/Run_1.png').convert_alpha()
    character2_run2_png = pygame.image.load('images/character/character2/run/Run_2.png').convert_alpha()
    character2_run3_png = pygame.image.load('images/character/character2/run/Run_3.png').convert_alpha()
    character2_run4_png = pygame.image.load('images/character/character2/run/Run_4.png').convert_alpha()
    character2_run5_png = pygame.image.load('images/character/character2/run/Run_5.png').convert_alpha()
    character2_run6_png = pygame.image.load('images/character/character2/run/Run_6.png').convert_alpha()

    character2_runattack1_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_1.png').convert_alpha()
    character2_runattack2_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_2.png').convert_alpha()
    character2_runattack3_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_3.png').convert_alpha()
    character2_runattack4_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_4.png').convert_alpha()
    character2_runattack5_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_5.png').convert_alpha()
    character2_runattack6_png = pygame.image.load(
        'images/character/character2/runattack/RunAttack_6.png').convert_alpha()

    character2_squat1_png = pygame.image.load('images/character/character2/squat/Squat_1.png').convert_alpha()
    character2_squat2_png = pygame.image.load('images/character/character2/squat/Squat_2.png').convert_alpha()
    character2_squat3_png = pygame.image.load('images/character/character2/squat/Squat_3.png').convert_alpha()
    character2_squat4_png = pygame.image.load('images/character/character2/squat/Squat_4.png').convert_alpha()

    character2_walk1_png = pygame.image.load('images/character/character2/walk/Walk_1.png').convert_alpha()
    character2_walk2_png = pygame.image.load('images/character/character2/walk/Walk_2.png').convert_alpha()
    character2_walk3_png = pygame.image.load('images/character/character2/walk/Walk_3.png').convert_alpha()
    character2_walk4_png = pygame.image.load('images/character/character2/walk/Walk_4.png').convert_alpha()
    character2_walk5_png = pygame.image.load('images/character/character2/walk/Walk_5.png').convert_alpha()
    character2_walk6_png = pygame.image.load('images/character/character2/walk/Walk_6.png').convert_alpha()

    character2_walkattack1_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_1.png').convert_alpha()
    character2_walkattack2_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_2.png').convert_alpha()
    character2_walkattack3_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_3.png').convert_alpha()
    character2_walkattack4_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_4.png').convert_alpha()
    character2_walkattack5_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_5.png').convert_alpha()
    character2_walkattack6_png = pygame.image.load(
        'images/character/character2/walkattack/WalkAttack_6.png').convert_alpha()

    character3_attack1_png = pygame.image.load('images/character/character3/attack/Attack_1.png').convert_alpha()
    character3_attack2_png = pygame.image.load('images/character/character3/attack/Attack_2.png').convert_alpha()
    character3_attack3_png = pygame.image.load('images/character/character3/attack/Attack_3.png').convert_alpha()
    character3_attack4_png = pygame.image.load('images/character/character3/attack/Attack_4.png').convert_alpha()
    character3_attack5_png = pygame.image.load('images/character/character3/attack/Attack_5.png').convert_alpha()
    character3_attack6_png = pygame.image.load('images/character/character3/attack/Attack_6.png').convert_alpha()

    character3_death1_png = pygame.image.load('images/character/character3/death/Death_1.png').convert_alpha()
    character3_death2_png = pygame.image.load('images/character/character3/death/Death_2.png').convert_alpha()
    character3_death3_png = pygame.image.load('images/character/character3/death/Death_3.png').convert_alpha()
    character3_death4_png = pygame.image.load('images/character/character3/death/Death_4.png').convert_alpha()
    character3_death5_png = pygame.image.load('images/character/character3/death/Death_5.png').convert_alpha()
    character3_death6_png = pygame.image.load('images/character/character3/death/Death_6.png').convert_alpha()
    character3_death7_png = pygame.image.load('images/character/character3/death/Death_7.png').convert_alpha()
    character3_death8_png = pygame.image.load('images/character/character3/death/Death_8.png').convert_alpha()

    character3_fallattack1_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_1.png').convert_alpha()
    character3_fallattack2_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_2.png').convert_alpha()
    character3_fallattack3_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_3.png').convert_alpha()
    character3_fallattack4_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_4.png').convert_alpha()
    character3_fallattack5_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_5.png').convert_alpha()
    character3_fallattack6_png = pygame.image.load(
        'images/character/character3/fallattack/FallAttack_6.png').convert_alpha()

    character3_hurt1_png = pygame.image.load('images/character/character3/hurt/Hurt_1.png').convert_alpha()
    character3_hurt2_png = pygame.image.load('images/character/character3/hurt/Hurt_2.png').convert_alpha()
    character3_hurt3_png = pygame.image.load('images/character/character3/hurt/Hurt_3.png').convert_alpha()
    character3_hurt4_png = pygame.image.load('images/character/character3/hurt/Hurt_4.png').convert_alpha()

    character3_idle1_png = pygame.image.load('images/character/character3/idle/Idle_1.png').convert_alpha()
    character3_idle2_png = pygame.image.load('images/character/character3/idle/Idle_2.png').convert_alpha()
    character3_idle3_png = pygame.image.load('images/character/character3/idle/Idle_3.png').convert_alpha()
    character3_idle4_png = pygame.image.load('images/character/character3/idle/Idle_4.png').convert_alpha()

    character3_jump1_png = pygame.image.load('images/character/character3/jump/Jump_1.png').convert_alpha()
    character3_jump2_png = pygame.image.load('images/character/character3/jump/Jump_2.png').convert_alpha()
    character3_jump3_png = pygame.image.load('images/character/character3/jump/Jump_3.png').convert_alpha()
    character3_jump4_png = pygame.image.load('images/character/character3/jump/Jump_4.png').convert_alpha()
    character3_jump5_png = pygame.image.load('images/character/character3/jump/Jump_5.png').convert_alpha()
    character3_jump6_png = pygame.image.load('images/character/character3/jump/Jump_6.png').convert_alpha()
    character3_jump7_png = pygame.image.load('images/character/character3/jump/Jump_7.png').convert_alpha()
    character3_jump8_png = pygame.image.load('images/character/character3/jump/Jump_8.png').convert_alpha()

    character3_jumpattack1_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_1.png').convert_alpha()
    character3_jumpattack2_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_2.png').convert_alpha()
    character3_jumpattack3_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_3.png').convert_alpha()
    character3_jumpattack4_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_4.png').convert_alpha()
    character3_jumpattack5_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_5.png').convert_alpha()
    character3_jumpattack6_png = pygame.image.load(
        'images/character/character3/jumpattack/JumpAttack_6.png').convert_alpha()

    character3_run1_png = pygame.image.load('images/character/character3/run/Run_1.png').convert_alpha()
    character3_run2_png = pygame.image.load('images/character/character3/run/Run_2.png').convert_alpha()
    character3_run3_png = pygame.image.load('images/character/character3/run/Run_3.png').convert_alpha()
    character3_run4_png = pygame.image.load('images/character/character3/run/Run_4.png').convert_alpha()
    character3_run5_png = pygame.image.load('images/character/character3/run/Run_5.png').convert_alpha()
    character3_run6_png = pygame.image.load('images/character/character3/run/Run_6.png').convert_alpha()

    character3_runattack1_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_1.png').convert_alpha()
    character3_runattack2_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_2.png').convert_alpha()
    character3_runattack3_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_3.png').convert_alpha()
    character3_runattack4_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_4.png').convert_alpha()
    character3_runattack5_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_5.png').convert_alpha()
    character3_runattack6_png = pygame.image.load(
        'images/character/character3/runattack/RunAttack_6.png').convert_alpha()

    character3_squat1_png = pygame.image.load('images/character/character3/squat/Squat_1.png').convert_alpha()
    character3_squat2_png = pygame.image.load('images/character/character3/squat/Squat_2.png').convert_alpha()
    character3_squat3_png = pygame.image.load('images/character/character3/squat/Squat_3.png').convert_alpha()
    character3_squat4_png = pygame.image.load('images/character/character3/squat/Squat_4.png').convert_alpha()

    character3_walk1_png = pygame.image.load('images/character/character3/walk/Walk_1.png').convert_alpha()
    character3_walk2_png = pygame.image.load('images/character/character3/walk/Walk_2.png').convert_alpha()
    character3_walk3_png = pygame.image.load('images/character/character3/walk/Walk_3.png').convert_alpha()
    character3_walk4_png = pygame.image.load('images/character/character3/walk/Walk_4.png').convert_alpha()
    character3_walk5_png = pygame.image.load('images/character/character3/walk/Walk_5.png').convert_alpha()
    character3_walk6_png = pygame.image.load('images/character/character3/walk/Walk_6.png').convert_alpha()

    character3_walkattack1_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_1.png').convert_alpha()
    character3_walkattack2_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_2.png').convert_alpha()
    character3_walkattack3_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_3.png').convert_alpha()
    character3_walkattack4_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_4.png').convert_alpha()
    character3_walkattack5_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_5.png').convert_alpha()
    character3_walkattack6_png = pygame.image.load(
        'images/character/character3/walkattack/WalkAttack_6.png').convert_alpha()

    characters = [[[character1_attack1_png, character1_attack2_png, character1_attack3_png, character1_attack4_png,
                    character1_attack5_png, character1_attack6_png],
                   [character1_death1_png, character1_death2_png, character1_death3_png, character1_death4_png,
                    character1_death5_png, character1_death6_png, character1_death7_png, character1_death8_png],
                   [character1_fallattack1_png, character1_fallattack2_png, character1_fallattack3_png,
                    character1_fallattack4_png, character1_fallattack5_png, character1_fallattack6_png],
                   [character1_hurt1_png, character1_hurt2_png, character1_hurt3_png, character1_hurt4_png],
                   [character1_idle1_png, character1_idle2_png, character1_idle3_png, character1_idle4_png],
                   [character1_jump1_png, character1_jump2_png, character1_jump3_png, character1_jump4_png,
                    character1_jump5_png, character1_jump6_png, character1_jump7_png, character1_jump8_png],
                   [character1_jumpattack1_png, character1_jumpattack2_png, character1_jumpattack3_png,
                    character1_jumpattack4_png, character1_jumpattack5_png, character1_jumpattack6_png],
                   [character1_run1_png, character1_run2_png, character1_run3_png, character1_run4_png,
                    character1_run5_png, character1_run6_png],
                   [character1_runattack1_png, character1_runattack2_png, character1_runattack3_png,
                    character1_runattack4_png, character1_runattack5_png, character1_runattack6_png],
                   [character1_squat1_png, character1_squat2_png, character1_squat3_png, character1_squat4_png],
                   [character1_walk1_png, character1_walk2_png, character1_walk3_png, character1_walk4_png,
                    character1_walk5_png, character1_walk6_png],
                   [character1_walkattack1_png, character1_walkattack2_png, character1_walkattack3_png,
                    character1_walkattack4_png, character1_walkattack5_png, character1_walkattack6_png]],
                  [[character2_attack1_png, character2_attack2_png, character2_attack3_png, character2_attack4_png,
                    character2_attack5_png, character2_attack6_png],
                   [character2_death1_png, character2_death2_png, character2_death3_png, character2_death4_png,
                    character2_death5_png, character2_death6_png, character2_death7_png, character2_death8_png],
                   [character2_fallattack1_png, character2_fallattack2_png, character2_fallattack3_png,
                    character2_fallattack4_png, character2_fallattack5_png, character2_fallattack6_png],
                   [character2_hurt1_png, character2_hurt2_png, character2_hurt3_png, character2_hurt4_png],
                   [character2_idle1_png, character2_idle2_png, character2_idle3_png, character2_idle4_png],
                   [character2_jump1_png, character2_jump2_png, character2_jump3_png, character2_jump4_png,
                    character2_jump5_png, character2_jump6_png, character2_jump7_png, character2_jump8_png],
                   [character2_jumpattack1_png, character2_jumpattack2_png, character2_jumpattack3_png,
                    character2_jumpattack4_png, character2_jumpattack5_png, character2_jumpattack6_png],
                   [character2_run1_png, character2_run2_png, character2_run3_png, character2_run4_png,
                    character2_run5_png, character2_run6_png],
                   [character2_runattack1_png, character2_runattack2_png, character2_runattack3_png,
                    character2_runattack4_png, character2_runattack5_png, character2_runattack6_png],
                   [character2_squat1_png, character2_squat2_png, character2_squat3_png, character2_squat4_png],
                   [character2_walk1_png, character2_walk2_png, character2_walk3_png, character2_walk4_png,
                    character2_walk5_png, character2_walk6_png],
                   [character2_walkattack1_png, character2_walkattack2_png, character2_walkattack3_png,
                    character2_walkattack4_png, character2_walkattack5_png, character2_walkattack6_png]],
                  [[character3_attack1_png, character3_attack2_png, character3_attack3_png, character3_attack4_png,
                    character3_attack5_png, character3_attack6_png],
                   [character3_death1_png, character3_death2_png, character3_death3_png, character3_death4_png,
                    character3_death5_png, character3_death6_png, character3_death7_png, character3_death8_png],
                   [character3_fallattack1_png, character3_fallattack2_png, character3_fallattack3_png,
                    character3_fallattack4_png, character3_fallattack5_png, character3_fallattack6_png],
                   [character3_hurt1_png, character3_hurt2_png, character3_hurt3_png, character3_hurt4_png],
                   [character3_idle1_png, character3_idle2_png, character3_idle3_png, character3_idle4_png],
                   [character3_jump1_png, character3_jump2_png, character3_jump3_png, character3_jump4_png,
                    character3_jump5_png, character3_jump6_png, character3_jump7_png, character3_jump8_png],
                   [character3_jumpattack1_png, character3_jumpattack2_png, character3_jumpattack3_png,
                    character3_jumpattack4_png, character3_jumpattack5_png, character3_jumpattack6_png],
                   [character3_run1_png, character3_run2_png, character3_run3_png, character3_run4_png,
                    character3_run5_png, character3_run6_png],
                   [character3_runattack1_png, character3_runattack2_png, character3_runattack3_png,
                    character3_runattack4_png, character3_runattack5_png, character3_runattack6_png],
                   [character3_squat1_png, character3_squat2_png, character3_squat3_png, character3_squat4_png],
                   [character3_walk1_png, character3_walk2_png, character3_walk3_png, character3_walk4_png,
                    character3_walk5_png, character3_walk6_png],
                   [character3_walkattack1_png, character3_walkattack2_png, character3_walkattack3_png,
                    character3_walkattack4_png, character3_walkattack5_png, character3_walkattack6_png]]]

    for i in range(len(characters)):
        for j in range(len(characters[i])):
            for w in range(len(characters[i][j])):
                sprite = pygame.sprite.Sprite()
                sprite.image = characters[i][j][w]
                sprite.rect = sprite.image.get_rect()
                sprite.mask = pygame.mask.from_surface(sprite.image)
                sprite.rect.x, sprite.rect.y = 0, 528
                characters[i][j][w] = sprite

    background = pygame.sprite.Group()
    player = pygame.sprite.Group()

    coords_platform = []

    def create_background(level):
        if level == 1:
            background.remove()
            background.empty()
            screen.blit(background1_png, (0, 0))
            k = 0
            for i in range(15):
                platform = pygame.sprite.Sprite()
                platform.image = pygame.image.load('images/for_levels/platform.png')
                platform.rect = sprite.image.get_rect()
                platform.rect.x, platform.rect.y = k, 570
                background.add(platform)
                coords_platform.append((k, 570))
                k += 30
            k = 700
            for i in range(7):
                platform = pygame.sprite.Sprite()
                platform.image = pygame.image.load('images/for_levels/platform.png')
                platform.rect = sprite.image.get_rect()
                platform.rect.x, platform.rect.y = k, 570
                background.add(platform)
                coords_platform.append((k, 570))
                k += 30
            k = 200
            for i in range(4):
                platform = pygame.sprite.Sprite()
                platform.image = pygame.image.load('images/for_levels/platform.png')
                platform.rect = sprite.image.get_rect()
                platform.rect.x, platform.rect.y = k, 490
                background.add(platform)
                coords_platform.append((k, 490))
                k += 30
            k = 540
            for i in range(2):
                platform = pygame.sprite.Sprite()
                platform.image = pygame.image.load('images/for_levels/platform.png')
                platform.rect = sprite.image.get_rect()
                platform.rect.x, platform.rect.y = k, 490
                background.add(platform)
                coords_platform.append((k, 490))
                k += 30
            for i in range(1):
                platform = pygame.sprite.Sprite()
                platform.image = pygame.image.load('images/for_levels/platform.png')
                platform.rect = sprite.image.get_rect()
                platform.rect.x, platform.rect.y = 420, 540
                background.add(platform)
                coords_platform.append((420, 540))
            background.draw(screen)
        elif level == 2:
            pass
        elif level == 3:
            pass
        elif level == 4:
            pass


    def change_player(group, n_character, animation, n_stage, x, y, inversion=0):
        try:
            group.remove()
            group.empty()
            if inversion:
                for i in range(len(characters[n_character - 1])):
                    for j in range(len(characters[n_character - 1][i])):
                        characters[n_character - 1][i][j].image = pygame.transform.flip(
                            characters[n_character - 1][i][j].image, True, False)
            characters[n_character - 1][animations[animation]][n_stage].rect.x = x
            characters[n_character - 1][animations[animation]][n_stage].rect.y = y
            characters[n_character - 1][animations[animation]][n_stage].mask = pygame.mask.from_surface(
                characters[n_character - 1][animations[animation]][n_stage].image)
            group.add(characters[n_character - 1][animations[animation]][n_stage])
        except Exception:
            pass


    create_background(1)
    running = True
    speed = 100  # пикселей в секунду
    jump_height = 9
    fps = 60
    clock = pygame.time.Clock()
    player_x, player_y = 0, 528
    is_update = True
    is_jump = False
    is_inversion = False
    is_right = True
    animation = 'idle'
    stage = 0
    character = 3
    count_events = 0
    level = 1
    change_player(player, character, animation, 0, player_x, player_y)
    player.draw(screen)
    while running:
        events = pygame.key.get_pressed()
        if not is_jump:
            if events[pygame.K_UP]:
                is_jump = True
                jump_height = 9
                animation = 'jump'
                stage = 0
                count_events += 1
        else:
            stage = (stage + 0.4) % len(characters[character - 1][animations[animation]])
            animation = 'jump'
            if jump_height >= -9:
                if jump_height > 0:
                    player_y -= (jump_height ** 2) / 2
                else:
                    player_y += (jump_height ** 2) / 2
                jump_height -= 1
            else:
                is_jump = False
            is_update = True

        if events[pygame.K_DOWN]:
            pass

        if events[pygame.K_RIGHT]:
            count_events += 1
            if not is_jump:
                animation = 'walk'
                stage = (stage + 0.25) % len(characters[character - 1][animations[animation]])
            if is_right:
                is_inversion = False
            else:
                is_inversion = True
            player_x += 8
            is_right = True
            is_update = True

        if events[pygame.K_LEFT]:
            count_events += 1
            if not is_jump:
                animation = 'walk'
                stage = (stage + 0.25) % len(characters[character - 1][animations[animation]])
            if is_right:
                is_inversion = True
            else:
                is_inversion = False
            player_x -= 8
            is_right = False
            is_update = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if is_update:
            intersection = False
            intersection2 = False
            create_background(level)
            old_x, old_y = 0, 528
            for player_mask in player:
                old_x, old_y = player_mask.rect.x, player_mask.rect.y
            change_player(player, character, animation, int(stage), player_x, player_y, is_inversion)
            is_inversion = False
            for el in background:
                for player_mask in player:
                    if pygame.sprite.collide_mask(player_mask, el):
                        intersection = True
            change_player(player, character, animation, int(stage), player_x, player_y, is_inversion)
            if intersection:
                player_x, player_y = old_x, old_y
                intersection = False
            change_player(player, character, animation, int(stage), player_x, player_y, is_inversion)
            if (count_events == 0) and not is_jump:
                animation = 'idle'
                stage = (stage + 0.15) % 3
            player.draw(screen)
            count_events = 0
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
