jQuery(function($) {
  const avater =
    "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4MCIgaGVpZ2h0PSI1NDAiIHZpZXdCb3g9IjAgMCAxMDgwIDU0MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZmlsbD0iI0VCRUJFQiIgZD0iTTAgMGgxMDgwdjU0MEgweiIvPgogICAgICAgIDxwYXRoIGQ9Ik00NDUuNjQ5IDU0MGgtOTguOTk1TDE0NC42NDkgMzM3Ljk5NSAwIDQ4Mi42NDR2LTk4Ljk5NWwxMTYuMzY1LTExNi4zNjVjMTUuNjItMTUuNjIgNDAuOTQ3LTE1LjYyIDU2LjU2OCAwTDQ0NS42NSA1NDB6IiBmaWxsLW9wYWNpdHk9Ii4xIiBmaWxsPSIjMDAwIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz4KICAgICAgICA8Y2lyY2xlIGZpbGwtb3BhY2l0eT0iLjA1IiBmaWxsPSIjMDAwIiBjeD0iMzMxIiBjeT0iMTQ4IiByPSI3MCIvPgogICAgICAgIDxwYXRoIGQ9Ik0xMDgwIDM3OXYxMTMuMTM3TDcyOC4xNjIgMTQwLjMgMzI4LjQ2MiA1NDBIMjE1LjMyNEw2OTkuODc4IDU1LjQ0NmMxNS42Mi0xNS42MiA0MC45NDgtMTUuNjIgNTYuNTY4IDBMMTA4MCAzNzl6IiBmaWxsLW9wYWNpdHk9Ii4yIiBmaWxsPSIjMDAwIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz4KICAgIDwvZz4KPC9zdmc+Cg==";

  const image =
    "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDUwMCA1MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxwYXRoIGZpbGw9IiNFQkVCRUIiIGQ9Ik0wIDBoNTAwdjUwMEgweiIvPgogICAgICAgIDxyZWN0IGZpbGwtb3BhY2l0eT0iLjEiIGZpbGw9IiMwMDAiIHg9IjY4IiB5PSIzMDUiIHdpZHRoPSIzNjQiIGhlaWdodD0iNTY4IiByeD0iMTgyIi8+CiAgICAgICAgPGNpcmNsZSBmaWxsLW9wYWNpdHk9Ii4xIiBmaWxsPSIjMDAwIiBjeD0iMjQ5IiBjeT0iMTcyIiByPSIxMDAiLz4KICAgIDwvZz4KPC9zdmc+Cg==";

  const content =
    "Your content goes here. Edit or remove this text inline or in the module Content settings. You can also style every aspect of this content in the module Design settings and even apply custom CSS to this text in the module Advanced settings.";

  if (
    window.ETBuilderBackendDynamic &&
    window.ETBuilderBackendDynamic.defaults
  ) {
    window.ETBuilderBackendDynamic.defaults.dnxte_flip_box = {
      front_heading: "Front Title Goes Here",
      back_heading: "Back Title Goes Here",
      front_content: `<p>${content}</p>`,
      back_content: `<p>${content}</p>`,
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_image_reveal = {
      dnext_img_reveal: avater,
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_3d_flipbox = {
      front_heading: "Front Title Goes Here",
      back_heading: "Back Title Goes Here",
      front_content:
        "<p>Your content goes here. Edit or remove this text inline or in the module Content settings. You can also style every aspect of this content in the module Design settings.</p>",
      back_content:
        "<p>Your content goes here. Edit or remove this text inline or in the module Content settings.</p>",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_team_social_reveal = {
      teamsorev_image: image,
      teamsorev_name: "Name Goes Here",
      teamsorev_position: "Position",
      teamsorev_content: content,
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_person = {
      teamperson_image: image,
      teamperson_name: "Name Goes Here",
      teamperson_position: "CEO and Founder , Unknown Company",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_team_overlay = {
      teamoverlay_image: image,
      teamoverlay_name: "Name Goes Here",
      teamoverlay_position: "CEO and Founder , Unknown Company",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_team_overlay_card = {
      teamoverlay_card_image: image,
      teamovelay_card_content: content,
      teamoverlay_card_name: "Name Goes Here",
      teamoverlay_card_position: "CEO and Founder , Unknown Company",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_team_creative = {
      team_creative_image: image,
      team_creative_name: "Name Goes Here",
      team_creative_position: "CEO and Founder , Unknown Company",
      button_text: "Button Text",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_review = {
      reviewer_image: image,
      reviewer_name: "Name Goes Here",
      reviewer_position: "CEO and Founder , Unknown Company",
      content: `<p>${content}</p>`,
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_image_icon = {
      dnxtiep_iie_image: avater,
      dnxtiep_iie_heading_text: "Heading Text",
      dnxtiep_iie_heading_bold: "Focus Text",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_mask = {
      text_mask: "Text Mask",
      thumbnail_image_mask: avater,
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_gradient_text = {
      gradient_title: "Gradient Heading Text",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_multi_heading = {
      text_one: "Multi",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_animation = {
      before_text: "Before Text",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_color_motion = {
      text_color_motion: "Heading",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_divider = {
      dnxt_divider_text: "Text Divider",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_glitch_text = {
      glitch_text: "Glitch",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_highlight = {
      highlight_text: "Highlight",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_highlight = {
      highlight_text: "Highlight",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_hover_highlight = {
      thh_before_text: "Before",
      thh_highlight_text: "Highlight",
      thh_after_text: "After",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_hover_highlight = {
      thh_before_text: "Before",
      thh_highlight_text: "Highlight",
      thh_after_text: "After",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_stroke = {
      dnxt_text_stroke_title: "Stroke Text",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_stroke_motion = {
      dnxt_text_stroke_title: "Stroke",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_stroke_motion = {
      stroke_text: "Stroke",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_text_tilt = {
      tilt_text: "Tilt Heading",
      tilt_body: "Lorem ipsum dolor sit, amet consectetur",
    };
    // Image Effect
    window.ETBuilderBackendDynamic.defaults.dnxte_mega_image_effect = {
      dnxtiep_image: avater,
      dnxtiep_heading_text: "Your Heading Text Goes Here",
      dnxtiep_description: content,
    };
    // Image Hover Box
    window.ETBuilderBackendDynamic.defaults.dnxte_image_hover_box = {
      dnxtiep_ihb_image: avater,
      dnxtiep_ihb_heading_text: "Your Heading Text Goes Here",
    };
    // Ultimate Image Hover
    window.ETBuilderBackendDynamic.defaults.dnxte_ultimate_image_hover = {
      dnxtiep_uih_image: avater,
      dnxtiep_uih_heading_text: "Heading Text",
      dnxtiep_uih_heading_bold: "Focus Text",
    };
    // Minimal Image Hover
    window.ETBuilderBackendDynamic.defaults.dnxte_minimal_image_hover = {
      image: avater,
    };
    // Circular Image Hover
    window.ETBuilderBackendDynamic.defaults.dnxte_circular_image_hover = {
      dnxtiep_cih_image: avater,
      dnxtiep_cih_heading_text: "Your Heading Text Goes Here",
      dnxtiep_cih_description:
        "Your content goes here. Edit or remove this text inline or in the module Content settings. You can also style every aspect of this content in the module Design",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_blurb = {
      dnxt_image: avater,
      blurb_heading: "Your Heading Text Goes Here",
      blurb_description: content,
      blurb_pre_heading: "Pre Heading Text",
      blurb_post_heading: "Post Heading Text",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_business_hour_child = {
      dnxte_businesshour_title: "Monday ",
      dnxte_businesshour_time: "9:00 AM - 6:00 PM ",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_price_list_child = {
      dnxte_pricelist_heading_text: "Title Text",
      dnxte_pricelist_price: "0$",
      dnxte_pricelist_description: content,
      dnxte_pricelist_image: avater,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_thumbs_gallery_child = {
      thumbs_gallery_top_image: avater,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_3dcubeslider_child = {
      cubeslider_image: avater,
      cubeslider_title: "Heading Goes Here ",
      cubeslider_content: content,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_coverflowslider_child = {
      coverflowslider_image: avater,
      coverflowslider_text: "Heading Goes Here",
      coverflowslider_content: content,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_logo_carousel_child = {
      logo_carousel_image: avater,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_testimonial_child = {
      dnxte_testimonial_name: "Name Goes Here",
      dnxte_testimonial_position: "Position Goes Here,",
      company_name: "Your Company Name",
      dnxte_testimonial_description: content,
      dnxte_testimonial_logo: image,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_promobox = {
      dnxte_promobox_title_one: "Product Support",
      dnxte_promobox_title_two: "Our Products are Customizable",
      dnxte_promobox_title_three: "Friendly Support",
      dnxte_promobox_button_text: "Buy Now",
      dnxte_promobox_offer_text: "30% off",
      dnxte_promobox_content: content,
      dnxte_promobox_image: image,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_feature_list_child = {
      dnxte_feature_list_title: "Title Goes Here",
      dnxte_feature_list_image: image,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_floating_element_child = {
      floting_shape_image: avater,
      floting_shape_text: "Text Goes Here",
    };
    window.ETBuilderBackendDynamic.defaults.dnxte_step_flow = {
      badge_title: "Pro-v1",
      dnxte_stepflow_title: "Share With Friends",
      dnxte_stepflow_description:
        "Create an excellent step by step visual diagram and instructions using this smart widget.",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_tooltip = {
      tooltip_image: avater,
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_lottie = {
      lottie_title: "Title Goes Here",
      lottie_content: content,
      lottie_button_text: "Click Here",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_image_magnifier = {
      magnifier_upload: avater,
      image_alt: "magnifier",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_timeline_child = {
      timeline_title: "Title Goes Here",
      timeline_content: content,
      timeline_button_text: "Read more",
      timeline_date: "Jan 14",
    };

    window.ETBuilderBackendDynamic.defaults.dnxte_image_accordion_item = {
      dnxte_imga_title: "Title Goes Here",
      dnxte_imga_des: content,
      button_text: "Read more",
    };
  }
});
