
let RoBotList = [];
class Robot{
    constructor(id)
    {
        this.$id = $(id);
        this.$id.on('click', function(e){
            if(e.which === 1)
            {
                let $chat_body = $('.chat-body');
                $chat_body.empty();
                $chat_body.append(`<div class="chat-header border-bottom py-xl-4 py-md-3 py-2">
                <div class="container-xxl">
                    <div class="row align-items-center">
                        <div class="col-6 col-xl-4">
                            <div class="media">
                                <div class="avatar me-3">
                                    <div class="avatar rounded-circle no-image bg-primary text-light">
                                        <span><i class="zmdi zmdi-comment-text"></i></span>
                                    </div>
                                </div>
                                <div class="media-body overflow-hidden">
                                    <div class="d-flex align-items-center mb-1">
                                        <h6 class="text-truncate mb-0 me-auto">Support ChatBot</h6>
                                    </div>
                                    <div class="text-truncate"><i class="zmdi zmdi-circle text-success"></i> Online
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-6 col-xl-8 text-end">
                        </div>
                    </div>
                </div>
            </div>`)
            }
            else if(e.which === 3)
            {

            }
        });
    }

}
let $creteButton = $('#newRobot')
$creteButton.on('click', function (e) {
    if(e.which === 1)
    {
        let $chatList = $('.chat-list');
        let $newBot = $(`<li class="active" id="robot_${RoBotList.length+1}">\n` +
            `                            <div class="card-body">\n` +
            '                                <div class="media">\n' +
            '                                    <div class="avatar me-3">\n' +
            '                                        <div class="avatar rounded-circle no-image bg-primary text-light">\n' +
            '                                            <span><i class="zmdi zmdi-comment-text"></i></span>\n' +
            '                                        </div>\n' +
            '                                    </div>\n' +
            '                                    <div class="media-body overflow-hidden">\n' +
            '                                        <div class="d-flex align-items-center mb-1">\n' +
            '                                            <h6 class="text-truncate mb-0 me-auto rotName">Support ChatBot</h6>\n' +
            '                                        </div>\n' +
            '                                        <div class="text-truncate">\n' +
            '                                            <i class="zmdi zmdi-circle text-success"></i> Online\n' +
            '                                        </div>\n' +
            '                                    </div>\n' +
            '                                </div>\n' +
            '                            </div>\n' +
            '                        </a>\n' +
            '                    </li>')
        
        $chatList.append($newBot)
        RoBotList.push(new Robot(`#robot_${RoBotList.length+1}`))
    }
})